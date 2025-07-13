# ASMR Agent

A Python-based ASMR agent that generates ASMR audio and video content using scripts and various utilities.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ibtihaajk7/asmr-agent.git
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   On Windows PowerShell, you should activate your virtual environment with:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
    

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the full pipeline

```bash
python scripts/run_pipeline.py
```

### Run individual generators:

```bash
python scripts/generate_individual.py
```

This will present you with a menu to choose which component to generate:
- **Script only** - Generates ASMR script using OpenAI
- **Audio only** - Generates audio from script (uses most recent session)
- **Video only** - Generates video with audio (uses most recent session)
- **All components** - Generates script, audio, and video in sequence

## Project Structure

```
asmr-agent/
├── src/                          # Source code
│   ├── generators/               # Generation modules
│   │   ├── script_generator.py  # OpenAI script generation
│   │   ├── audio_generator.py   # Resemble AI audio generation
│   │   └── video_generator.py   # Pexels video generation
│   ├── utils/                    # Utility modules
│   │   └── pexels_utils.py      # Pexels API utilities
│   └── config/                   # Configuration
│       └── constants.py         # Constants and session management
├── scripts/                      # Executable scripts
│   ├── run_pipeline.py          # Full pipeline runner
│   └── generate_individual.py   # Individual generator runner
├── assets/                       # Static assets
│   └── background_audio/        # Background audio files for videos
├── output/                       # Generated content (session folders)
├── tests/                        # Test files
└── docs/                         # Documentation
```

## License

MIT
