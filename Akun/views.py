# from django.views.generic.edit import FormView
# from django.urls import reverse_lazy
# from django.shortcuts import render, redirect


# from .forms import FormPendaftaran

# class PendaftaranView(FormView):
#     template_name = 'registration/sigup.html'
#     success_url = reverse_lazy('Akun:index')

#     def get_form(self, form_clas=None):
#         form_class = FormPendaftaran
#         return form_class(**self.get_form_kwargs())

#     def post(self, *args, **kwargs):
#         form = self.get_form(self.request.POST)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
    
#     def form_valid(self, form):
#         form.save()
#         return redirect(self.success_url)

#     def form_invalid(self, form):
#         return render(self.request, self.template_name, {"form": form})

# def pendaftaran(request):
#     template = 'registration/sigup.html'
#     if request.method == 'POST':
#         form = FormPendaftaran(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('Akun:index'))
#         return render(request, template, {'form':form})
#     form = FormPendaftaran
#     return render(request, template, {'form':form})