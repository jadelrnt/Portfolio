def convert(msg):
    msg = msg.replace(":)" , "🙂").replace(":(", "🙁")
    return msg
def main():
    msg = input("Write something : ")
    result = convert(msg)
    print(result)
main()
