Hi, This is T.S.Balagurunadhaswamy, applying for the role of Django Developer. To set up this package all you need to
do is run the command

The virtual environment has to be activated in order to run the application. It can be done by locating the file called "venv", Once that file is 
located run command

'source venv/bin/activate'

Which will activate the virtual environment. After that the packeges that I have used must be downloaded.

All the packages that I have used are in the requirements.txt.

'pip install -r requirements.txt'

Run the above command to install all the packages. Once that is done all that is left to do is start the application.

To start the application locate the 'manage.py' file. And in that location run 

'python manage.py runserver' 

Once that is done the home page will be in 'http://127.0.0.1:8000/'

There the login button is visible. You can use the credentials 'ash' as username and '1' as password. You can also 
create a new user from the addmin panel. But please make sure that the User that you have created is Mapped with the
Employee model. That too can be done from the admin panel. 

Once you are logged in Click on the 'Tender Page' button to go to the "Tender proposal Form"

The details of the user are automatically fetched from the request and the sender details are prepopulated!

Fill only the "Proposal Summary", "Project Planning" and "Financing Details". I have used "Textarea" tag for all the fields
for the sole reason of keeping everything multilined!

I was asked not to use packages or libraries, But I had to use jsPDF to generate the pdf. The pdf generation is client side.

Once the form is filled, the pdf can be generated using the Generate button and the Submit button saves the document.

I had initially asked for extention as my laptop had issues and because of that I coudn't complete the drag and drop feature,
my apologies for that!

Please reach out to me for any doubts or clarifications!

More importantly the user can log out using the "Logout" button on the right corner. I am not very good at UI designs. 
So I went in a minimalistic ay without any UI designs. 

I am very well aware that the downloaded pdf does not a good format, But as I said earlier, I genuinly did not have time to look into it as my laptop
had issues and I had to lose 2 days because of that.