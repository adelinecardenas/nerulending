from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = 'whitelabelpartnerportal'
urlpatterns = [
    url('^$', login_required(HomeWhiteLabelView.as_view(), login_url='/user/login'),
        name='home-whitelabel'),
    url('whitelabeltraining', login_required(WhiteLabelTrainingView.as_view(), login_url='/user/login'),
        name='whitelabeltraining'),
    url('myresiduals', login_required(MyResidualsView.as_view(), login_url='/user/login'),
        name='myresiduals'),
    url('enternewleads', login_required(EnterNewLeadsView.as_view(), login_url='/user/login'),
        name='enternewleads'),
    url('marketingroi', login_required(MarketingRoiView.as_view(), login_url='/user/login'),
        name='marketingroi'),
    path('becomingapartner/edit/<int:pk>', BecomingAPartner_update, name='becomingapartner_edit'),
    path('leadoverview/edit/<int:pk>', lead_update, name='lead_edit'),
    path('salesaffiliates/edit/<int:pk>', affiliate_agent_update, name='affiliate_agent_edit'),
    path('addbankinfo/edit/<int:pk>', bank_info_update, name='paypal_info_update'),
    path('addpaypalinfo/edit/<int:pk>', paypal_info_update, name='bank_info_update'),
    path('create_account', CreateAccountView.as_view(), name='create_account'),
    path('client-created-by-you', ClientCreatedByYouView.as_view(), name='clients-created-by-you'),
    path('addzelleinfo/edit/<int:pk>', zelle_info_update, name='zelle_info_update'),
    url('leadoverview', login_required(LeadOverviewView.as_view(), login_url='/user/login'),
        name='leadoverview'),
    url('mysales', login_required(MySalesView.as_view(), login_url='/user/login'),
        name='mysales'),
    url('networkmarketing', login_required(NetworkMarketingView.as_view(), login_url='/user/login'),
        name='networkmarketing'),
    url(r'becomingapartner$', login_required(BecomingAPartnerView.as_view(), login_url='/user/login'),
        name='becomingapartner'),
    url('becomingapartner1$', login_required(BecomingAPartnerView1.as_view(), login_url='/user/login'),
        name='becomingapartner1'),
    url('enteraffiliates', login_required(EnterAffiliatesView.as_view(), login_url='/user/login'),
        name='enteraffiliates'),
    url('salesaffiliates', login_required(SalesAffiliatesView.as_view(), login_url='/user/login'),
        name='salesaffiliates'),
    url('residualsfromaffiliates', login_required(ResidualsFromAffiliatesView.as_view(), login_url='/user/login'),
        name='residualsfromaffiliates'),
    url('freesignup', login_required(FreeSignupView.as_view(), login_url='/user/login'),
        name='freesignup'),
    url('paidsignup', login_required(PaidSignupView.as_view(), login_url='/user/login'),
        name='paidsignup'),
    url('orders', login_required(OrdersView.as_view(), login_url='/user/login'),
        name='orders'),
    url('invoices', login_required(InvoicesView.as_view(), login_url='/user/login'),
        name='invoices'),
    url('payments', login_required(PaymentsView.as_view(), login_url='/user/login'),
        name='payments'),
    url('credits', login_required(CreditsView.as_view(), login_url='/user/login'),
        name='credits'),
    url('wholesalepackages', login_required(WholesalePackagesView.as_view(), login_url='/user/login'),
        name='wholesalepackages'),
    url('offeringfinancing', login_required(OfferingFinancingView.as_view(), login_url='/user/login'),
        name='offeringfinancing'),
    url('whitelabelwebinar', login_required(WhiteLabelWebinarView.as_view(), login_url='/user/login'),
        name='whitelabelwebinar'),
    url('buywhitelabelwebsite', login_required(BuyWhitelabelWebsiteView.as_view(), login_url='/user/login'),
        name='buywhitelabelwebsite'),
    url('buywhitelabelbusinesspackage',
        login_required(BuyWhitelabelBusinessPackageView.as_view(), login_url='/user/login'),
        name='buywhitelabelbusinesspackage'),
    url('viewportals', login_required(ViewPortalsView.as_view(), login_url='/user/login'),
        name='viewportals'),
    url('viewwhitelabelwebsite', login_required(ViewWhiteLabelWebsiteView.as_view(), login_url='/user/login'),
        name='viewwhitelabelwebsite'),
    url('viewwhitelabelbusinesspackage',
        login_required(ViewWhiteLabelBusinessPackageView.as_view(), login_url='/user/login'),
        name='viewwhitelabelbusinesspackage'),
    url('addbankinfo_form', login_required(AddBankInfoFormView.as_view(), login_url='/user/login'),
        name='addbankinfo_form'),
    url('addbankinfo', login_required(AddBankInfoView.as_view(), login_url='/user/login'),
        name='addbankinfo'),

    url('addpaypalinfo_form', login_required(AddPaypalInfoFormView.as_view(), login_url='/user/login'),
        name='addpaypalinfo_form'),
    url('addzelleinfoform', login_required(AddZelleInfoFormView.as_view(),
        login_url='/user/login'), name="addzelleinfo_form"),
    url('addpaypalinfo', login_required(AddPaypalInfoView.as_view(), login_url='/user/login'),
        name='addpaypalinfo'),
    url('addzelleinfo', login_required(addZelleInfoView.as_view(),
        login_url='/user/login'), name='addzelleinfo'),
    
    url('merchant', login_required(MerchantView.as_view(), login_url='/user/login'),
        name='merchant'),
    url('fax', login_required(FaxView.as_view(), login_url='/user/login'),
        name='fax'),
    url('tollfree', login_required(TollFreeView.as_view(), login_url='/user/login'),
        name='tollfree'),
    url('professionalemail', login_required(ProfessionalEmailView.as_view(), login_url='/user/login'),
        name='professionalemail'),
    url('partnercommisssions', login_required(PartnerCommissionView.as_view(), login_url='/user/login'),
        name='partnercommisssions'),

    url('productmanagement', login_required(ProductManagementView.as_view(), login_url='/user/login'),
        name='productmanagement'),

    url('wholesales', login_required(WholesaleView.as_view(), login_url='/user/login'),
        name='wholesales'),
    url('^clients_on_wholesale', login_required(ClientsOnWholesaleView.as_view(), login_url='/user/login'),
        name='clients-on-wholesale'),
    url('^partner_resources', login_required(PartnerResourceView.as_view(), login_url='/user/login'),
        name='partner_resources'),

    path('manageportal', login_required(ManageWhitelabel.as_view(), login_url='/user/login'),
        name='manageportal'),
    url('client_progress', login_required(ClientProgress.as_view(), login_url='/user/login'),
        name='clientProgress'),

    url('add_client_portal', login_required(AddClientPortals.as_view(), login_url='/user/login'),
        name='add_client_portal'),

    url('^edit_wholesaleee$', login_required(EditWholesale.as_view(), login_url='/user/login'), name='edit_wholesaleee'),
    url('^edit_softwares$', login_required(EditSoftware.as_view(), login_url='/user/login'), name='edit_softwares'),
    url('edit_tradelines', login_required(EditTradeline.as_view(), login_url='/user/login'), name='edit_tradelines'),
    url('edit_usersteps', login_required(EditUserSteps.as_view(), login_url='/user/login'), name='edit_usersteps'),

]