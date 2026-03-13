import torch
from fourm.models.generate import build_chained_generation_schedules, init_empty_target_modality, init_full_input_modality
from fourm.data.modality_info import MODALITY_INFO, MODALITY_TRANSFORMS
from tokenizers import Tokenizer

def create_generation_schedule_rgb_to_others(target_domains,
                                             decoding_steps, temps,
                                             cfg_scales, img, cfg_grow_conditioning=True
                                             ):
    """
    Create RGB to any other conditional domain
    """
    text_tok = Tokenizer.from_file('./text_tokenizer_4m_wordpiece_30k.json')
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    tokens_per_target_dict = {
        'tok_clip@224': 196,
        'tok_dinov2@224': 256,
        'tok_imagebind@224': 256,
        'tok_depth@224': 196,
        'tok_normal@224': 196,
        'tok_semseg@224': 196,
        'tok_canny_edge@224': 196,
        'tok_sam_edge@224': 196,
        'caption': 256,
        'det': 256,
        'human_poses': 275,
        'sam_instance': 256,
        'color_palette': 23,
        'metadata': 40
    }

    autoregression_schemes_dict = {
        'tok_clip@224': 'roar',
        'tok_dinov2@224': 'roar',
        'tok_imagebind@224': 'roar',
        'tok_depth@224': 'roar',
        'tok_normal@224': 'roar',
        'tok_semseg@224': 'roar',
        'tok_canny_edge@224': 'roar',
        'tok_sam_edge@224': 'roar',
        'caption': 'autoregressive',
        'det': 'autoregressive',
        'human_poses': 'autoregressive',
        'sam_instance': 'autoregressive',
        'color_palette': 'autoregressive',
        'metadata': 'autoregressive'
    }

    cfg_schedules_dict = {
        'tok_clip@224': 'constant',
        'tok_dinov2@224': 'constant',
        'tok_imagebind@224': 'constant',
        'tok_depth@224': 'constant',
        'tok_normal@224': 'constant',
        'tok_semseg@224': 'constant',
        'tok_canny_edge@224': 'constant',
        'tok_sam_edge@224': 'constant',
        'caption': 'constant',
        'det': 'constant',
        'human_poses': 'constant',
        'sam_instance': 'constant',
        'color_palette': 'constant',
        'metadata': 'constant'
    }

    cond_domain = ['rgb@224']
    cfg_schedules = [cfg_schedules_dict[target_domain] for target_domain in target_domains]
    temp_schedules = cfg_schedules
    autoregression_schemes = [autoregression_schemes_dict[target_domain] for target_domain in target_domains]
    tokens_per_targets = [tokens_per_target_dict[target_domain] for target_domain in target_domains]
    token_decoding_schedules = ['linear' if 'tok_' in target_domain else None for target_domain in target_domains]
    schedule = build_chained_generation_schedules(
        cond_domains=cond_domain,
        target_domains=target_domains,
        tokens_per_target=tokens_per_targets,
        autoregression_schemes=autoregression_schemes,
        decoding_steps=decoding_steps,
        token_decoding_schedules=token_decoding_schedules,
        temps=temps,
        temp_schedules=temp_schedules,
        cfg_scales=cfg_scales,
        cfg_schedules=cfg_schedules,
        cfg_grow_conditioning=cfg_grow_conditioning
    )

    batched_sample = {
        'rgb@224': {
            'tensor': img,  # Batched tensor
            'input_mask': torch.zeros(1, 196, dtype=torch.bool, device=device),  # False = used as input, True = ignored
            'target_mask': torch.ones(1, 196, dtype=torch.bool, device=device),
            # False = predicted as target, True = ignored
        }
    }

    # Initialize target modalities
    for target_mod, ntoks in zip(target_domains, tokens_per_targets):
        batched_sample = init_empty_target_modality(batched_sample, MODALITY_INFO, target_mod, 1, ntoks, device)

    # Initialize input modalities
    for cond_mod in cond_domain:
        batched_sample = init_full_input_modality(batched_sample, MODALITY_INFO, cond_mod, device,
                                                  eos_id=text_tok.token_to_id("[EOS]"))

    return schedule, batched_sample