from requests import session
import getpass
import requests
from bs4 import BeautifulSoup


def urlGrabber():

  def downloader(url):
    repoName = url.split("/");

    # import the requests library
    import requests; 
     
    # download the file contents in binary format
    r = requests.get(url);
    dest = repoName[-3] + ".zip";
    # open method to open a file on your system and write the contents
    with open( dest + ".zip", "wb") as code:
        code.write(r.content);
     

    s.get(url);


  USER = input("Please enter your GitHub account name (You will need an authorized account to download private repositories): ");
  PASSWORD = getpass.getpass();

  URL1 = 'https://github.com/session'
  URL2 = 'https://github.com/LC-Data?tab=repositories'


  with session() as s:

    req = s.get(URL1).text
    html = BeautifulSoup(req)
    token = html.find("input", {"name": "authenticity_token"}).attrs['value']
    com_val = html.find("input", {"name": "commit"}).attrs['value']        

    login_data = {'login': USER,
                  'password': PASSWORD,
                  'commit' : com_val,
                  'authenticity_token' : token}

    r1 = s.post(URL1, data = login_data)
    r2 = s.get(URL2)

    #print(token)
    #print(r1.text)
    #print(r2.text)


    url = input("Please enter the URL from the account's main repository page (should end in '?tab=repositories'):  ");

    response = s.get(url, timeout=55000)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = []

    for link in soup.find_all('a'):
        print("IS THIS THE USERNAME?!!?!?!?!?!?!?!?!?!", link.get('href').split("/"))
        repoUser = USER;
        print(link.get('href'))
        print(len(link.get('href').split("/")))

        if (link.get('href')[-4:] == ".zip"):
          repoDownload(link.get('href'))

        elif (len(link.get('href').split("/")) == 3 and (link.get('href').split("/")[1] == repoUser)):
          print("\n\n\n\n GOT EM");
          links.append(link.get('href'))
          print(str(link.get('href')) + " WAS APPENDED TO THE FINAL DOWNLOAD LIST...");
          print(links)

        elif (len(link.get('href').split("/")) != 3):
          print("\n   DO NOT GOOOOOT!!!!!")
          print(link.get('href'))

          
    print(links)

    links2 = links[:-5]  #removes other github bullshit -- eventually just try and regex for a repository name structure and exclude what this line cuts out
    print("\n\n\n\n\n")
    print(links2)


    for repo in links2:
      preUrl = URL2[:-17].split("/") #trim off the unneeded bits of the url, then split it at the /s to seperate path in to list items
      print(preUrl) 
      preUrlFinal = preUrl[0] + "//" + preUrl[2];   #this concats "http:" + "//" + "github.com/TARGETUSER"
      print("THIS IS THE PREEEEEEEEEEEEEEUUUUUUUUUURRRRRRRRLLLLLLLLFINAL!!!    ", preUrlFinal)
      repo = preUrlFinal + repo + "/archive/master.zip";
      print("INITIATING DOWNLOAD OF " + str(repo));

      downloader(repo)


urlGrabber();
