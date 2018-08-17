with open("name.txt","r") as names:
    with open("body.txt","r") as bodys:
        body = bodys.read()
        for name in names:
            mail = "Hello"+name+body
            with open(name.strip() + ".txt", 'w') as mail_file:
                mail_file.write(mail)