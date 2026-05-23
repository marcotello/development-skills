import json
import argparse
import os

# Simplified logic for managing the state.json
def manage_state():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', choices=['update', 'complete'])
    parser.add_argument('--linear-id')
    parser.add_argument('--session-id')
    parser.add_argument('--repo')
    args = parser.parse_args()

    state_path = 'assets/state.json'
    
    if not os.path.exists(state_path):
        data = {"tasks": []}
    else:
        with open(state_path, 'r') as f:
            data = json.load(f)

    if args.action == 'update':
        data['tasks'].append({
            "linear_id": args.linear_id,
            "session_id": args.session_id,
            "repo": args.repo,
            "status": "IN_PROGRESS"
        })
    
    elif args.action == 'complete':
        for task in data['tasks']:
            if task['linear_id'] == args.linear_id:
                task['status'] = "COMPLETED"

    with open(state_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    manage_state()
