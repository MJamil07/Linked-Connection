from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import SignUpUser , Jops , AppCompanies , Job_Posts , Apply_jop , UserFollow , Post
from datetime import date


def auth(request):
    if 'exist' not in request.session:
        return redirect(chooseUser)

def chooseUser(request):
    
    if 'exist' in request.session:
        return redirect(home)
    return render(request , "startPage.html");


def home(request):
    if 'exist' not in request.session:
        return redirect(chooseUser)
    existingUser = ''
    isEmploye = True;

    print(Job_Posts.objects.all().filter(companie = 1)[0].position)
    try:
        if request.session['userType'] == 'employee':
            existingUser = SignUpUser.objects.get(email = request.session['username'])
            isEmploye = True
        else:
            existingUser = AppCompanies.objects.get(gmail = request.session['username'] )
            isEmploye = False
    except:
        print('err')
    companies = AppCompanies.objects.all()
    return render(request , 'homes/home.html' , {'jops' : Job_Posts.objects.all() ,  'newUser' : existingUser , 'companies' : companies , 'Users' : SignUpUser.objects.all()})

def logout(request):

    try:
        del request.session['exist']
        del request.session['username']
        del request.session['userType']
    except:
        pass
    return redirect(chooseUser)

def signIn(request , types):

    if 'exist' in request.session :
        return redirect(home)
    
    if  types == 'employee' or types == 'company':
        request.session['userType'] = types;
        print(request.session['userType'])

    

    if request.method == 'POST':
        user_name = request.POST['email'];
        password = request.POST['password'];

        
        if request.session['userType'] == 'employee' and SignUpUser.objects.filter(email = user_name).exists() and SignUpUser.objects.filter(password = password).exists() :
            request.session['exist'] = True;
            request.session['username'] = user_name;
            return redirect(home)
    
        if request.session['userType'] == 'company' and AppCompanies.objects.filter(gmail = request.POST['email']).exists() and AppCompanies.objects.filter(password = request.POST['password']).exists() :
            request.session['exist'] = True;
            request.session['username'] = request.POST['email'];
            return redirect(home)

    return render(request , 'signin.html')

def signUp(request):

    isEmployee = False;
    if request.session['userType'] == 'employee':
        isEmployee = True;

    if request.method == 'POST':
        try:
            if isEmployee:
                SignUpUser.objects.create(first_name =  request.POST['firstName'] , last_name = request.POST['lastName'] , email = request.POST['email'] , password = request.POST['password'] , college_name = request.POST['collegename'] , qualification = request.POST['qualification'] ,  phone = request.POST['phone']   )
            else :
                print('is now')
                AppCompanies.objects.create(name = request.POST['companyname'] , size = request.POST['companysize'] , head = request.POST['headQ'], about = request.POST['about'], based = request.POST['based'], products = request.POST['products'], website = request.POST['website'], gmail = request.POST['email'], password = request.POST['password'], phone = request.POST['phone'], type = request.POST['companytype'], logo = request.POST['companylogo'])
                
        except Exception as e:
            print(e)
            return redirect(signUp)
        
        return redirect(signIn , 'none')

    return render(request , 'signup.html' , {'formFilter' : isEmployee})


def company_profile(request):
    auth(request)
    currUser = AppCompanies.objects.get(gmail = request.session['username']);
    id = currUser.id;  # type: ignore
    jop_lists = Job_Posts.objects.filter(companie = id)
    print(jop_lists)

    if request.method == 'POST':
        Job_Posts.objects.create(position = request.POST['position'] , type = request.POST['type'],description = request.POST['describtion'],location= request.POST['location'],post_date = '2022-12-05' ,responsibility = request.POST['responsibility'],basic_qualification = request.POST['b_qualify'],preffered_qualification = request.POST['p_qualify'], companie = currUser)
        company_profile(request)
    
    
    return render(request , 'homes/Profile.html'  , {'company' : currUser , 'jop_lists' : jop_lists , 'NoOfJops' : len(jop_lists)})



def view_job(request , id):

    auth(request)
    
    print('Hey')
    
    user_choose_jop = Job_Posts.objects.get(id = id);
    
    related_jop_position = Job_Posts.objects.filter(position = user_choose_jop.position); 
      
    return render(request , 'applyjop.html' , {'jop' : user_choose_jop , 'related' : related_jop_position})

def jop_apply(request):
    auth(request)
    
    if request.method == 'POST':
        if request.session['userType'] == 'company':
            print('now')
            return redirect(home)
        print('Incoming')
    
        Apply_jop.objects.create(name = request.POST['applyername'] , skills = request.POST['skills'] , user = SignUpUser.objects.get(email = request.session['username']), jop_post = Job_Posts.objects.get(id = request.POST['id']))
  
    return redirect(home)

def viewed_appply(request , id):
    auth(request)

    user_apply_jop = Apply_jop.objects.filter(jop_post = id)
    return render(request , 'viewedjop.html' , {'jop_applyer' : user_apply_jop , 'count_the_jop' : len(user_apply_jop)  } )

def user_view(request , id):
    auth(request)

    # get incoming user details
    choose_user =  SignUpUser.objects.get(id = id);
    followings = UserFollow.objects.filter(froms = choose_user.email).count()
    followers = UserFollow.objects.filter(to = choose_user.email).count()

    return render(request , 'userProfile.html' , 
        {'user' : choose_user ,
         'followings' : followings,
         'followers' : followers
          })

def choose_profile(request):
    auth(request)

    if request.session['userType'] == 'company':
        return redirect(company_profile)
    
    return redirect(user_view , SignUpUser.objects.get(email = request.session['username']).id )  # type: ignore
    
def follow(req , id):
    
    # get the current user email
    froms = SignUpUser.objects.get(email = req.session['username'])  # type: ignore

    # check curr user is eqaul incoming id user
    if id == froms.id:  # type: ignore
        return redirect(home)
    
    # get incoming user information
    to = SignUpUser.objects.get(id = id)  # type: ignore

    # current user incase already follow return home
    if len(UserFollow.objects.filter(froms = "mjamil@gmail.com" , to = to.email)) > 0:
        return redirect(home)

    # create a follow and followings
    UserFollow.objects.create(froms = froms.email , to = to.email )  # type: ignore

    return redirect(home)

def post(request):

    if request.method == 'POST':

        if request.session['userType'] == 'company':
            companie = AppCompanies.objects.get(gmail = request.session['username'])  # type: ignore 
            Post.objects.create(description = request.POST.get('description') , image = request.POST.get('image') , companie = companie)
            return redirect(company_profile)

        else:
            user = SignUpUser.objects.get(email = request.session['username']) # type: ignore 
            Post.objects.create(description = request.POST.get('description') , image = request.POST.get('image') , user = user)
            return redirect(user_view , user.id)  # type: ignore
    else:

        return redirect(home)
    
def jops(request):

    return render(request , "jops.html" , {'jops' : Job_Posts.objects.all()})

def companies(request):

    return render(request , "companies.html" , {'companies' : AppCompanies.objects.all()})
