from rest_framework_nested import routers
from bvs.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
)
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

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")

router.register(r"user", UserViewSet, basename="user")

router.register(r"donor", DonorViewSet, basename="donor")
router.register(r"occupation", OccupationViewSet, basename="occupation")
router.register(r"ethnic", EthnicViewSet, basename="ethnic")
router.register(r"family", FamilyViewSet, basename="family")
router.register(r"religion", ReligionViewSet, basename="religion")


router.register(r"patient", PatientViewSet, basename="patient")
patients_router = routers.NestedSimpleRouter(router, r"patient", PatientViewSet, lookup="patient")
patients_router.register(r"treatment", TreatmentViewSet, basename="patient-treatment")
patients_router.register(r"funding", FundingViewSet, basename="patient-funding")
patients_router.register(r"pshychosocial", PsychosocialViewSet, basename="pshychosocial-funding")
patients_router.register(r"physiotherapy", PhysiotherapyViewSet, basename="physiotherapy-funding")

urlpatterns = [*router.urls, *patients_router.urls]
