import os
import h5py
import pandas as pd

root_dir = r"C:\Users\alecp\OneDrive\Documents\Grad School\Spring 2025 Classes\Big Data - CS-GY 6513\Final Project\millionsongsubset\MillionSongSubset"

def extract_track_metadata(h5_path):
    with h5py.File(h5_path, 'r') as f:
        song_data = f['metadata']['songs'][0]
        analysis_data = f['analysis']['songs'][0]

        # Extracting relevant fields by name
        def get(field, group='metadata'):
            if group == 'metadata':
                return song_data[f['metadata']['songs'].dtype.names.index(field)]
            elif group == 'analysis':
                return analysis_data[f['analysis']['songs'].dtype.names.index(field)]

        return {
            'track_id': get('track_id').decode('utf-8'),
            'title': get('title').decode('utf-8'),
            'artist_name': get('artist_name').decode('utf-8'),
            'year': get('year'),
            'duration': get('duration', group='analysis'),
            'tempo': get('tempo', group='analysis'),
            'loudness': get('loudness', group='analysis')
        }

# Recursively collect .h5 file paths
h5_files = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".h5"):
            h5_files.append(os.path.join(root, file))

# Optional: limit for quick testing
# h5_files = h5_files[:100]

# Extract all track metadata
data = []
for path in h5_files:
    try:
        record = extract_track_metadata(path)
        data.append(record)
    except Exception as e:
        print(f"Error reading {path}: {e}")

# Create DataFrame
df = pd.DataFrame(data)

print(df.head())
