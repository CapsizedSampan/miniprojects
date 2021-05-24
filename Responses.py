from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text.lower())

    if user_message in ("hello", "hi", "yo"):
        return "Hi, how you doin?"

    if user_message in ("time left", "time?"):
        now = datetime.now()
        end = datetime.strptime("12/05/21, 17:30:00","%d/%m/%y, %H:%M:%S")
        print(f"end:{end}")
        diff = end - now
        exist = str(diff)
        #deadline = datetime.strftime(exist,"%H:%M:%S")

        #print("exist:", exist)
        final = exist.split(".")
        #print("list", final)
        last = final[:-1]
        #print("last", last)
        #print(final)
        return last[0]

    if user_message in ("no", "dumb"):
        return ":("
