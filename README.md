# Readme for ELIS v0.1

ELIS is a free, open-sourced tool that aims to help users find the right therapist. 

Version v0.1 is limited to 
- search only
- therapists located in Vienna (AT)
- therapists with websites

## Database

Our database is compiled from the publicly available list of Psychotherapists [[Berufsliste (Psychotherapie)](https://psychotherapie.ehealth.gv.at/)]. The related API offers numerous endpoints. To access them, please contact us for an access key. 

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
- Valid API key (contact us @openelis)
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
