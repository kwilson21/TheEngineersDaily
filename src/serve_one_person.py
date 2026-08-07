import argparse

def serve_person(args):
    print("Requirement: {p} needs to {t} so that {s}.".format(p=args.person, t=args.task,s=args.success))    

def main():
    parser = argparse.ArgumentParser(prog='Serve One Person')
    
    parser.add_argument('--person', help='The name of the person we are serving', required=True)

    parser.add_argument('--task', help='The task we are performing to serve the person', required=True)

    parser.add_argument('--success', required=True)

    args = parser.parse_args()

    serve_person(args)

if __name__ == "__main__":
    main()