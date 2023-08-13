#!/usr/bin/env python3
"""
Main analyzef1 script
"""
import logging
import subprocess
from pathlib import Path

import fastf1 as ff1

logger = logging.getLogger("F1InsightX")


def main():
    # subprocess.run(['python3', '-m', 'streamlit', 'run', 'analyzef1/Home.py'])
    subprocess.run("streamlit run Home.py", shell=True)


if __name__ == "__main__":
    cachefolder = f"{Path().resolve()}/cache"
    Path(cachefolder).mkdir(parents=True, exist_ok=True)
    ff1.Cache.enable_cache(cachefolder)
    logger.info(f"Using cache folder: {cachefolder}")
    main()
