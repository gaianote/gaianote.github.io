import os

# os.chdir("docs") 

if os.path.exists("docs/_sidebar.md"):
   os.remove("docs/_sidebar.md")
current_path = "docs"
for path,dir_list,file_list in os.walk("docs"):
    for filename in file_list:
        if filename.endswith(".md") and not filename.startswith("_") and filename not in ("README.md"):
            if current_path != path:
                space = "  " * (len(path.split("/"))-1)
                dirname = path.split("/")[-1]
                line = "{}- [{}]({}/{})\n".format(space,dirname,path,"README.md").replace("docs/","")
                with open("docs/_sidebar.md","a+") as f:
                    f.write(line)        
                # 把文件写进目录
                space = "  " * (len(path.split("/")))
                line = "{}- [{}]({}/{})\n".format(space,filename.split(".md")[0],path,filename).replace("docs/","")
                with open("docs/_sidebar.md","a+") as f:
                    f.write(line)
                current_path = path
            else:
                space = "  " * (len(path.split("/")))
                line = "{}- [{}]({}/{})\n".format(space,filename.split(".md")[0],path,filename).replace("docs/","")
                with open("docs/_sidebar.md","a+") as f:
                    f.write(line)    