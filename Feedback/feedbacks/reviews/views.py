from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import View
from .forms import ReviewForm
from .models import Review 
from django.views.generic.base import TemplateView # ye bhi ek view hota ahi ajb sirf html file return krna hota hai 
from .models import Review
from django.views.generic import ListView,DetailView# ye bhi ek view hota ahi ajb sirf html file return krna hota hai 
from django.views.generic.edit import FormView,CreateView

# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
        
#         return render(request,"reviews/review.html",{
#             "form":form
#         })
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")
        
#         return render(request,"reviews/review.html",{
#             "form":form
#         })

# form view ka code hai ye 
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     # uper ke code so wo apne aap hi get wlaa handle kr lega 
#     success_url = "thank-you"
    
#     #for saving in db 
#     def form_valid(self, form):  
#         form.save()
#         return super().form_valid(form)

    #for saving in db 
# form view ka end hai ye

#createview ka code hai ye 
class ReviewView(CreateView):
    model = Review 
    form_class=ReviewForm 
    template_name = "reviews/review.html"
    success_url = "thank-you"
    
  
#createview ak code end ho gya hai 

# def review(request):
#     if request.method == 'POST':
        
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")
#             #  review = Review(user_name=form.cleaned_data['user_name'],
#             #                  review_text = form.cleaned_data['review_text'],
#             #                  rating= form.cleaned_data['rating']
#             #                  )
#             #  review.save()
#             # ye uppar wala tab likhte hai jab user form aur model same na ho.
            
            
             
#           #   print(form.cleaned_data)
          
        
#         # entered_username = request.POST['username'] # isme request.POST ek dictionary hai of all name values in input form 
#         # if entered_username == "" :
#         #     return render(request, "reviews/review.html", {
#         #         "has_error": True
#         #     })
#         # return HttpResponseRedirect("/thank-you")
    
#     else:
#         form = ReviewForm()
    
#     # Yeh return hamesha hona chahiye (GET aur POST invalid dono ke liye)
#     return render(request, "reviews/review.html", {
#         # "has_error": False
#         "form": form
#     })

#converting th thank_you into class view (part-2)
# class ThankYouView(View):
    
#     def get(self,request):
#         return render(request, "reviews/thank-you.html")

#(part-1)
# def thank_you(request):
#     return render(request, "reviews/thank-you.html")

#   (part-3)
class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This one is working 💐"
        return context

# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context   

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review   # ✅ singular rakho
#         return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review 
    # jab hum isme html template me use krte hai to usme object_list se data apss on hota hai 
    context_object_name = "reviews"
    
    # def  get_queryset(self):
    #     base_query=super().get_queryset()
    #     return base_query.filter(rating__gt=4)


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    
