print("Users with login shells, or non-default users:")
print("%-20s\t%s" % ("User", "Shell"))
with open("/etc/passwd") as f:
    for line in f.readlines():
        sep = line.strip().split(":")
        if (int(sep[2]) > 1000 and int(sep[2]) < 65534) or (sep[6] != "/bin/false" and sep[6] != "/usr/sbin/nologin"):
            print("%-20s\t%s" % (sep[0], sep[6]))
