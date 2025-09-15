#!/bin/bash
#SBATCH --job-name=crosstalk
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=380000M
#SBATCH --output=logs/crosstalk_%j.out
#SBATCH --error=logs/crosstalk_%j.err

set -euo pipefail
mkdir -p logs
cd "$SLURM_SUBMIT_DIR"


# Run with uv using your project .venv; pass any args to enamine.py via sbatch
srun --cpu-bind=cores uv run python enamine.py 