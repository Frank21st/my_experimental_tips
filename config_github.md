the following steps are used to config github

s1    config the user.name and user.email.

	git config --user.name 'your_user_name_on_github_website'

	git config --user.email 'you_email_on_github_website@email_server.com'


s2    generate ssh

	ssh-keygen -t rsa -C 'your_eamil_on_github_website@email_server.com'


s3    get the content of  id_rsa.pub

    you can use the command:  cat /User/user_name/.ssh/id_rsa.pub

    then copy it.


s4    copy the content of id_rsa.pub to SSH Keys on github


s5    run command : ssh -T git@github.com 
   
	 and choose 'yes' when encounting "are you want to continue onnecting (yes/no/[fingerprint])?".

	 after that, one file will be created and you can git clone repository.
