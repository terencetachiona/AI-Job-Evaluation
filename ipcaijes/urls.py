from django.contrib import admin
from django.urls import include, path
from aijes.views import aijes, employees, supervisors, evaluators

urlpatterns = [
    path('', include('aijes.urls')),
    path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', aijes.SignUpView.as_view(), name='signup'),
    path('accounts/signup/employee/', employees.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('accounts/signup/supervisor/', supervisors.SupervisorSignUpView.as_view(), name='supervisor_signup'),
	path('accounts/signup/evaluator/', evaluators.EvaluatorSignUpView.as_view(), name='evaluator_signup'),

]