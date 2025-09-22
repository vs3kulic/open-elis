# Readme for ELIS v0.1

ELIS is free, open-sourced tool that aims to help users find the right therapist. 

Version v0.1 is limited to 
- search only
- therapists located in Vienna (AT)
- therapists with websites

## Database

Our database is compiled from the publicly available list of Psychotherapist [<INSERT SOURCE>]. The related API offers numerous endpoints. To access them, please [<SIGN UP>] for an access key. We recommend reviewing the [<API DOCUMENTATION>] to explore the extensive datasets available.

## Parameters

- Geographical preference: location by district
- Therapist preferences: age group
- Personal preferences: pth. method (school)

## Requirements

### System Requirements
- Python 3.8+
- SQLite
- some disk space (for database)

### API Access
- Valid API key (sign up at [registration endpoint])
- HTTPS-enabled application for secure key transmission

### Development Setup
```bash
# Clone repository
git clone [repository-url]
cd elis

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r [requirements.txt](http://_vscodecontentref_/0)

# Run the application
uvicorn main:app --reload
```
