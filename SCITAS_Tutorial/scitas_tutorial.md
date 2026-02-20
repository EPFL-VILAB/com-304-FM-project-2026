# SCITAS Tutorial


- [SCITAS Tutorial](#scitas-tutorial)
- [What is SCITAS](#what-is-scitas)
- [Terminology](#terminology)
- [How to create an account](#how-to-create-an-account)
- [How to access to the cluster](#how-to-access-to-the-cluster)
  - [Login](#login)
  - [Volumes](#volumes)
    - [Home](#home)
    - [Scratch](#scratch)
  - [Upload data](#upload-data)
- [Running a job on the cluster](#running-a-job-on-the-cluster)
  - [Submitting a job](#submitting-a-job)
  - [GPU resources](#gpu-resources)
  - [Using Apptainer/Singularity to containerize your job](#using-apptainersingularity-to-containerize-your-job)
- [House keeping](#house-keeping)

---
# What is SCITAS
In COM-304 Communications Project, we are going to use the Scientific IT and Application Support (SCITAS) [[link](https://scitas-doc.epfl.ch/)] cluster for computation. It provides compute services to everyone at EPFL. Currently, it contains four clusters: Helvetios, Izar, Kuma, and Jed [[link](https://scitas-doc.epfl.ch/supercomputers/overview/)]. We will mainly use [Kuma](https://scitas-doc.epfl.ch/supercomputers/kuma/) as one option for the homeworks/exercises.

# Terminology
When you see ***locally*** or ***on your own computer***, it means the command should be executed on your own computer, not the cluster.

When you see ***remotely*** or ***on the clusters***, it means the command should be executed on the clusters (after logging in), not your own computer.

We use `<username>` to denote your username on the clusters. Please replace it with your actual username when you execute the commands.

# How to create an account
No need to do it yourself. Once you have enrolled yourself in the course, an account will be created automatically for you that uses your EPFL Gaspar credentials. Your account will be associated with the COM-304 project to use reserved GPUs or acquire high priority in job queues. Please reach out to the teaching staff in case you face any difficulty in using your account.
# How to access to the cluster
To connect to the clusters, you have to be inside the EPFL network or [establish a VPN connection](https://www.epfl.ch/campus/services/en/it-services/network-services/remote-intranet-access/vpn-clients-available/) [[link](https://scitas-doc.epfl.ch/user-guide/using-clusters/connecting-to-the-clusters/)].

## Login
You can access the clusters by using `ssh` on your own computer. You will need to provide your gaspar `<username>` and `<password>` to login. The command is:
```bash
ssh -X <username>@kuma.hpc.epfl.ch
```

## Volumes
The volumes mentioned below are the folders existing on the clusters.

### Home
You have 100 GB quota in `/home/<username>` for storing important files such as codes. The data in this directory is kept permanently.

### Scratch
`/scratch/<username>` is used to store large datasets, checkpoints, etc. Files here are **NOT backed up** and the files **older than 30 days will get deleted**. Therefore, only store files here that you can afford to lose and reproduce easily.

## Upload data
Sometimes, you need to upload data to the clusters or download data from the clusters [[link](https://scitas-doc.epfl.ch/user-guide/data-management/transferring-data/)]. On your own computer, you can use `rsync` [[link](https://scitas-doc.epfl.ch/user-guide/data-management/transferring-data/#using-rsync)] (recommended) and `scp` [[link](https://scitas-doc.epfl.ch/user-guide/data-management/transferring-data/#using-scp)] if you prefer command line tools. If you prefer GUI applications, you can also use [WinSCP](https://winscp.net/eng/index.php) on Windows or [FileZilla](https://filezilla-project.org/) on MacOS and Linux locally.

# Running Jobs on the Cluster

The SCITAS clusters use [SLURM](https://slurm.schedmd.com/documentation.html) to manage and schedule jobs. It is one of the most widely used job scheduling systems for HPC clusters. You can find comprehensive documentation on the [official SLURM site](https://slurm.schedmd.com/documentation.html) or by searching online.

There are **two main ways** to request compute resources and run your work on the cluster:

| Method | Best for |
|---|---|
| **Interactive session** (`srun`) | Debugging, exploration, quick experiments |
| **Batch job** (`sbatch`) | Long training runs, automated pipelines |

---

## Option 1 — Interactive Session

An interactive session gives you a live shell directly on a compute node with the resources you requested. This is useful when you want to test code, debug issues, or explore the environment before committing to a full job.

Use `srun` to start one:

```bash
srun -t 120 -A com-304 --qos=com-304 --gres=gpu:2 --mem=16G --cpus-per-task=6 -p l40s --pty bash
```

Here is what each flag means:

- `-t 120` — maximum session duration in minutes (here, 2 hours)
- `-A com-304` — account to charge resources to
- `--qos=com-304` — quality-of-service partition for the COM-304 course
- `--gres=gpu:2` — request 2 GPUs
- `--mem=16G` — request 16 GB of RAM
- `--cpus-per-task=6` — request 6 CPU cores
- `-p l40s` — use the `l40s` GPU partition
- `--pty bash` — open an interactive bash shell

Once the session starts, you will be dropped into a shell on the compute node and can run commands directly — for example launching Python scripts, testing CUDA, or inspecting your data. The session ends when you exit or when the time limit is reached.

> **Note:** Interactive sessions are great for development, but avoid using them for long training runs since the job will be killed if you lose your connection.

---

## Option 2 — Batch Job (sbatch)

For longer or automated workloads, you should submit a batch job using `sbatch`. You write a script that specifies both the resources you need and the commands to run, then submit it to the queue. SLURM will schedule and run it for you, even if you log out.


1. Create a file called `first_trial.run` (or any name ending in `.run` or `.sh`) with the following content:
    ```bash
       #!/bin/bash
       #SBATCH --chdir /home/
       #SBATCH --gres=gpu:1
       #SBATCH --nodes 1
       #SBATCH --ntasks 1
       #SBATCH --cpus-per-task 1
       #SBATCH --mem 4096
       #SBATCH --time 12:30:00
       #SBATCH --output /home//logs/%j.out
       #SBATCH --account=com-304
       #SBATCH --qos=com-304
       #SBATCH --partition=l40s
    
       echo STARTING AT `date`
       python --version
       echo FINISHED at `date`
    ```
   Let’s digest the commands a bit
   1. All the commands starting with `#SBATCH` specify the resources required for the job
      1. `#SBATCH --chdir /home/<username>` sets the working directory to be `/home/<username>`. All the commands are executing under this directory.
      2. `#SBATCH --nodes 1` sets the number of nodes required for the job to be `1`. In this course, you normally will only need 1 node for computation.
      3. `#SBATCH --ntasks 1` sets the number of parallel tasks to be `1`. In this course, you normally will only need 1 parallel task per job.
      4. `#SBATCH --cpus-per-task 1` sets the number of CPUs per task to be `1`. You can increase this number if your job is CPU intensive.
      5. `#SBATCH --mem 4096` sets the amount of memory for the job to be 4096MB.
      6. `#SBATCH --time 12:30:00` sets the maximum living time of the job to be 12.5 hrs.
      7. `#SBATCH --output /home/<username>/logs/%j.out` sets the output from the job to be logged into `#SBATCH --output /home/<username>/logs/%j.out` files. `%j` denotes the job id.
      8. `#SBATCH --account=com-304` and `#SBATCH --reservation=Course-com-304` specify that we are using the GPUs reserved for the COM-304 course.
      9. `#SBATCH --partition=l40s` specify which partition we would like to use in Kuma cluster
   2. The remaining commands are working scripts for training, etc. Here it simply prints the start and ending time of the script and the `python` version used.
      ```bash
      echo STARTING AT `date`
      python --version
      echo FINISHED at `date`
      ```
   For more information about the `xxx.run` file, you can check the `sbatch` page [[link](https://slurm.schedmd.com/sbatch.html)].

2. Submit the `first_trial.run` by `sbatch first_trial.run` on the clusters.
3. After submitting the job, you will see an immediate output `Submitted batch job 123456`. It means the job id is `123456`. Each job id is unique on the SLURM system.
4. You can cancel your job by running `scancel <job-id>`
5. To check the status of all your jobs, you can run `squeue -u <username>`.
Once the job finishes, check the output log at `/home/<username>/logs/123456.out`.



## Quick Reference

| Task | Command |
|---|---|
| Start an interactive session | `srun -t 120 -A com-304 --qos=com-304 --gres=gpu:2 --mem=16G --cpus-per-task=6 -p l40s --pty bash` |
| Submit a batch job | `sbatch first_trial.run` |
| Check your job queue | `squeue -u <username>` |
| Cancel a job | `scancel <job-id>` |



# House keeping

- Please be considerate to the other students when using the clusters.
- Note that the allowed number of GPUs for different exercises varies depending on the compute required to complete each exercise. Specific details about the allowed resources are included in the respective exercise documentation.