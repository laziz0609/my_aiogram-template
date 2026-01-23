content = "t = 30 , m_s =5 , b =60"
new_content = ""
for con in content:
    if con.isdigit() or con == ",":
        new_content += con
        
infos = new_content.split(",")
print(infos)