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
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the full pipeline:

```bash
python scripts/run_pipeline.py
```

### Run individual generators:

```bash
# Generate script only
python scripts/generate_individual.py script

# Generate audio (uses most recent session)
python scripts/generate_individual.py audio

# Generate video (uses most recent session)
python scripts/generate_individual.py video

# Generate audio for specific session
python scripts/generate_individual.py audio output/asmr_session_20241201_143022_001
```

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
├── output/                       # Generated content (session folders)
├── tests/                        # Test files
└── docs/                         # Documentation
```

## License

MIT
