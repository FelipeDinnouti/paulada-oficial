![Check out this site if you need more help](https://realpython.com/python-virtual-environments-a-primer/)

Using the venv (linux recommended, maybe only works on linux? check out the site to figure out if it works on Windows)

activate the venv
``` shell
$ source bin/activate
```
and 
``` shell
$ deactivate
```
to exit


## TODO

I need to start using this frequently.
Currently on branch "staging" I need to figure out some things.
Make hamburger menu is a fun thing
And making the "Login" and "Cadastro" buttons dissapear and get replaced by "Perfil" once you login. THAT CAN BE DONE WITH classes and javascript or just javascript

Figure out the login and register pages and make them responsive in the sense that: it checks if the email is actually an email.
In the registering area it checks with the SERVER if the user is already registered, then the SERVER returns a response to the CLIENT if the user is already registrated and proceeds to the next page (email verification)
That requires a lot of HTMX and basically HTMX only.
So basically there will be only ONE page related to profile.
That profile page will handle: Login, Register and Profile. All with HTMX.

The other pages will be handles as different pages. not with HTMX.
Mixing this is not good practice but it is a good practice of HTML knowledge.

Next thing I need to figure out is enhacing the infrastructure, to support a higher demand of traffic.l