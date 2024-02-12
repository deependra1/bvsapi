from rest_framework_nested import routers
from bvs.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
    PasswordChangeViewSet,
    ForgotPasswordViewSet,
)
from bvs.followUpSummary.viewsets import FollowUpSummaryViewSet

from bvs.user.viewsets import UserViewSet

from bvs.patient.viewsets import PatientViewSet
from bvs.treatment.viewsets import TreatmentViewSet
from bvs.donor.viewsets import DonorViewSet
from bvs.occupation.viewsets import OccupationViewSet
from bvs.ethnic.viewsets import EthnicViewSet
from bvs.family.viewsets import FamilyViewSet
from bvs.religion.viewsets import ReligionViewSet
from bvs.funding.viewsets import FundingViewSet
from bvs.pshychosocial.viewsets import PsychosocialViewSet
from bvs.physiotherapy.viewsets import PhysiotherapyViewSet
from bvs.burntype.viewsets import BurnTypeViewSet
from bvs.burncause.viewsets import BurnCauseViewSet
from bvs.question.viewsets import QuestionViewSet
from bvs.reintegration.viewsets import ReintegrationViewSet
from bvs.hospital.viewsets import HospitalViewSet
from bvs.educationlevel.viewsets import EducationLevelViewSet
from bvs.language.viewsets import LanguageViewSet


router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")
router.register(r"auth/password-change", PasswordChangeViewSet, basename="auth-password-change")
router.register(r'auth/forgot-password', ForgotPasswordViewSet, basename='auth-forgot-password')
router.register(r'auth/password-reset-confirm', ForgotPasswordViewSet, basename='auth-password-reset-confirm')

router.register(r"user", UserViewSet, basename="user")

router.register(r"donor", DonorViewSet, basename="donor")
router.register(r"occupation", OccupationViewSet, basename="occupation")
router.register(r"ethnic", EthnicViewSet, basename="ethnic")
router.register(r"family", FamilyViewSet, basename="family")
router.register(r"religion", ReligionViewSet, basename="religion")
router.register(r"burn_type", BurnTypeViewSet, basename="burn_type")
router.register(r"burn_cause", BurnCauseViewSet, basename="burn_cause")
router.register(r"question", QuestionViewSet, basename="question")
router.register(r"hospital", HospitalViewSet, basename="hospital")
router.register(r"educationlevel", EducationLevelViewSet, basename="educationlevel")
router.register(r"language", LanguageViewSet, basename="language")
router.register(r"follow-up-summary", FollowUpSummaryViewSet, basename="follow-up-summary")

router.register(r"treatment", TreatmentViewSet, basename="patient-treatment")
router.register(r"funding", FundingViewSet, basename="patient-funding")
router.register(r"pshychosocial", PsychosocialViewSet, basename="pshychosocial-funding")
router.register(r"physiotherapy", PhysiotherapyViewSet, basename="physiotherapy-funding")

router.register(r"patient", PatientViewSet, basename="patient")
patients_router = routers.NestedSimpleRouter(router, r"patient", PatientViewSet, lookup="patient")
patients_router.register(r"treatment", TreatmentViewSet, basename="patient-treatment")
patients_router.register(r"funding", FundingViewSet, basename="patient-funding")
patients_router.register(r"pshychosocial", PsychosocialViewSet, basename="pshychosocial-funding")
patients_router.register(r"physiotherapy", PhysiotherapyViewSet, basename="physiotherapy-funding")
patients_router.register(r"reintegration", ReintegrationViewSet, basename="patient-reintegration")

urlpatterns = [*router.urls, *patients_router.urls]
