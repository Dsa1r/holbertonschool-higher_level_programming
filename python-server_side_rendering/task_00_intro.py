def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(output)