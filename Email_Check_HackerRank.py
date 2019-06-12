# Valid email addresses must follow these rules:
#
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is 3.
def fun(s):
    # return True if s is a valid email, else return False
    if s.count("@") == 1 and s.count(".")==1:
        username , url  = s.split("@")
        website, extension = url.split(".")
        if len(extension)<=3:
            if website.isalnum():
                if username.replace("_","").isalnum() or username.replace("-","").isalnum():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)