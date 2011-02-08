# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Access(models.Model):
    aid = models.IntegerField(primary_key=True)
    mask = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    status = models.IntegerField()
    class Meta:
        db_table = u'access'

class Accesslog(models.Model):
    aid = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=192)
    title = models.CharField(max_length=765, blank=True)
    path = models.CharField(max_length=765, blank=True)
    url = models.TextField(blank=True)
    hostname = models.CharField(max_length=384, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    timer = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'accesslog'

class Actions(models.Model):
    aid = models.CharField(max_length=765, primary_key=True)
    type = models.CharField(max_length=96)
    callback = models.CharField(max_length=765)
    parameters = models.TextField()
    description = models.CharField(max_length=765)
    class Meta:
        db_table = u'actions'

class ActionsAid(models.Model):
    aid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'actions_aid'

class AdvancedHelpIndex(models.Model):
    sid = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=765)
    topic = models.CharField(max_length=765)
    language = models.CharField(max_length=36)
    class Meta:
        db_table = u'advanced_help_index'

class AggregatorCategory(models.Model):
    cid = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=765)
    description = models.TextField()
    block = models.IntegerField()
    class Meta:
        db_table = u'aggregator_category'

class AggregatorCategoryFeed(models.Model):
    fid = models.IntegerField()
    cid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'aggregator_category_feed'

class AggregatorCategoryItem(models.Model):
    iid = models.IntegerField()
    cid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'aggregator_category_item'

class AggregatorFeed(models.Model):
    fid = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=765)
    url = models.CharField(unique=True, max_length=765)
    refresh = models.IntegerField()
    checked = models.IntegerField()
    link = models.CharField(max_length=765)
    description = models.TextField()
    image = models.TextField()
    etag = models.CharField(max_length=765)
    modified = models.IntegerField()
    block = models.IntegerField()
    class Meta:
        db_table = u'aggregator_feed'

class AggregatorItem(models.Model):
    iid = models.IntegerField(primary_key=True)
    fid = models.IntegerField()
    title = models.CharField(max_length=765)
    link = models.CharField(max_length=765)
    author = models.CharField(max_length=765)
    description = models.TextField()
    timestamp = models.IntegerField(null=True, blank=True)
    guid = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'aggregator_item'

class Authmap(models.Model):
    aid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    authname = models.CharField(unique=True, max_length=384)
    module = models.CharField(max_length=384)
    class Meta:
        db_table = u'authmap'

class BackupMigrateDestinations(models.Model):
    destination_id = models.CharField(max_length=96, primary_key=True)
    name = models.CharField(max_length=765)
    type = models.CharField(max_length=96)
    location = models.TextField()
    settings = models.TextField()
    class Meta:
        db_table = u'backup_migrate_destinations'

class BackupMigrateProfiles(models.Model):
    profile_id = models.CharField(max_length=96, primary_key=True)
    name = models.CharField(max_length=765)
    filename = models.CharField(max_length=150)
    append_timestamp = models.IntegerField()
    timestamp_format = models.CharField(max_length=42)
    filters = models.TextField()
    class Meta:
        db_table = u'backup_migrate_profiles'

class BackupMigrateSchedules(models.Model):
    schedule_id = models.CharField(max_length=96, primary_key=True)
    name = models.CharField(max_length=765)
    source_id = models.CharField(max_length=96)
    destination_id = models.CharField(max_length=96)
    profile_id = models.CharField(max_length=96)
    keep = models.IntegerField()
    period = models.IntegerField()
    last_run = models.IntegerField()
    enabled = models.IntegerField()
    cron = models.IntegerField()
    class Meta:
        db_table = u'backup_migrate_schedules'

class Batch(models.Model):
    bid = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=192)
    timestamp = models.IntegerField()
    batch = models.TextField(blank=True)
    class Meta:
        db_table = u'batch'

class BetterFormatsDefaults(models.Model):
    rid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=765, primary_key=True)
    format = models.IntegerField()
    type_weight = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'better_formats_defaults'

class Blocks(models.Model):
    bid = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=192)
    delta = models.CharField(unique=True, max_length=96)
    theme = models.CharField(max_length=192)
    status = models.IntegerField()
    weight = models.IntegerField()
    region = models.CharField(max_length=192)
    custom = models.IntegerField()
    throttle = models.IntegerField()
    visibility = models.IntegerField()
    pages = models.TextField()
    title = models.CharField(max_length=192)
    cache = models.IntegerField()
    class Meta:
        db_table = u'blocks'

class BlocksRoles(models.Model):
    module = models.CharField(max_length=192, primary_key=True)
    delta = models.CharField(max_length=96, primary_key=True)
    rid = models.IntegerField()
    class Meta:
        db_table = u'blocks_roles'

class Book(models.Model):
    mlid = models.IntegerField(primary_key=True)
    nid = models.IntegerField(unique=True)
    bid = models.IntegerField()
    class Meta:
        db_table = u'book'

class Boxes(models.Model):
    bid = models.IntegerField(primary_key=True)
    body = models.TextField(blank=True)
    info = models.CharField(unique=True, max_length=384)
    format = models.IntegerField()
    class Meta:
        db_table = u'boxes'

class Cache(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache'

class CacheBlock(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_block'

class CacheContent(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_content'

class CacheFilter(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_filter'

class CacheForm(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_form'

class CacheMenu(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_menu'

class CacheMollom(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_mollom'

class CachePage(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_page'

class CacheRules(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_rules'

class CacheUpdate(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_update'

class CacheViews(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_views'

class CacheViewsData(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_views_data'

class CaptchaPoints(models.Model):
    form_id = models.CharField(max_length=384, primary_key=True)
    module = models.CharField(max_length=192, blank=True)
    type = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'captcha_points'

class CaptchaSessions(models.Model):
    csid = models.IntegerField()
    uid = models.IntegerField()
    sid = models.CharField(max_length=192)
    ip_address = models.CharField(max_length=384, blank=True)
    timestamp = models.IntegerField()
    form_id = models.CharField(max_length=384)
    solution = models.CharField(max_length=384)
    status = models.IntegerField()
    attempts = models.IntegerField()
    class Meta:
        db_table = u'captcha_sessions'

class CkeditorRole(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    rid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'ckeditor_role'

class CkeditorSettings(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'ckeditor_settings'

class CommentUpload(models.Model):
    fid = models.IntegerField()
    nid = models.IntegerField()
    cid = models.IntegerField()
    description = models.CharField(max_length=765)
    list = models.IntegerField()
    weight = models.IntegerField()
    legacy_fid = models.IntegerField()
    class Meta:
        db_table = u'comment_upload'

class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    pid = models.IntegerField()
    nid = models.IntegerField()
    uid = models.IntegerField()
    subject = models.CharField(max_length=192)
    comment = models.TextField()
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    status = models.IntegerField()
    format = models.IntegerField()
    thread = models.CharField(max_length=765)
    name = models.CharField(max_length=180, blank=True)
    mail = models.CharField(max_length=192, blank=True)
    homepage = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'comments'

class Contact(models.Model):
    cid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=765)
    recipients = models.TextField()
    reply = models.TextField()
    weight = models.IntegerField()
    selected = models.IntegerField()
    class Meta:
        db_table = u'contact'

class ContentFieldAssignmentAttachments(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_assignment_attachments_fid = models.IntegerField(null=True, blank=True)
    field_assignment_attachments_list = models.IntegerField(null=True, blank=True)
    field_assignment_attachments_data = models.TextField(blank=True)
    delta = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'content_field_assignment_attachments'

class ContentFieldContentAttachments(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    delta = models.IntegerField(primary_key=True)
    field_content_attachments_fid = models.IntegerField(null=True, blank=True)
    field_content_attachments_list = models.IntegerField(null=True, blank=True)
    field_content_attachments_data = models.TextField(blank=True)
    class Meta:
        db_table = u'content_field_content_attachments'

class ContentFieldDocumentAttachment(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    delta = models.IntegerField(primary_key=True)
    field_document_attachment_fid = models.IntegerField(null=True, blank=True)
    field_document_attachment_list = models.IntegerField(null=True, blank=True)
    field_document_attachment_data = models.TextField(blank=True)
    class Meta:
        db_table = u'content_field_document_attachment'

class ContentFieldProfileUrl(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    delta = models.IntegerField(primary_key=True)
    field_profile_url_url = models.CharField(max_length=765, blank=True)
    field_profile_url_title = models.CharField(max_length=765, blank=True)
    field_profile_url_attributes = models.TextField(blank=True)
    class Meta:
        db_table = u'content_field_profile_url'

class ContentGroup(models.Model):
    group_type = models.CharField(max_length=96)
    type_name = models.CharField(max_length=96, primary_key=True)
    group_name = models.CharField(max_length=96, primary_key=True)
    label = models.CharField(max_length=765)
    settings = models.TextField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'content_group'

class ContentGroupFields(models.Model):
    type_name = models.CharField(max_length=96, primary_key=True)
    group_name = models.CharField(max_length=96, primary_key=True)
    field_name = models.CharField(max_length=96, primary_key=True)
    class Meta:
        db_table = u'content_group_fields'

class ContentNodeField(models.Model):
    field_name = models.CharField(max_length=96, primary_key=True)
    type = models.CharField(max_length=381)
    global_settings = models.TextField()
    required = models.IntegerField()
    multiple = models.IntegerField()
    db_storage = models.IntegerField()
    module = models.CharField(max_length=381)
    db_columns = models.TextField()
    active = models.IntegerField()
    locked = models.IntegerField()
    class Meta:
        db_table = u'content_node_field'

class ContentNodeFieldInstance(models.Model):
    field_name = models.CharField(max_length=96, primary_key=True)
    type_name = models.CharField(max_length=96, primary_key=True)
    weight = models.IntegerField()
    label = models.CharField(max_length=765)
    widget_type = models.CharField(max_length=96)
    widget_settings = models.TextField()
    display_settings = models.TextField()
    description = models.TextField()
    widget_module = models.CharField(max_length=381)
    widget_active = models.IntegerField()
    class Meta:
        db_table = u'content_node_field_instance'

class ContentTypeAnnouncement(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_announcement_detail_value = models.TextField(blank=True)
    field_announcement_detail_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_announcement'

class ContentTypeAssignment(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_assignment_due_date_value = models.CharField(max_length=60, blank=True)
    field_assignment_sub_list_vname = models.CharField(max_length=96, blank=True)
    field_assignment_sub_list_vargs = models.CharField(max_length=765, blank=True)
    field_assignment_detail_value = models.TextField(blank=True)
    field_assignment_detail_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_assignment'

class ContentTypeCourse(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_course_status_value = models.TextField(blank=True)
    field_course_dates_value = models.CharField(max_length=60, blank=True)
    field_course_dates_value2 = models.CharField(max_length=60, blank=True)
    field_course_opening_date_value = models.CharField(max_length=60, blank=True)
    field_course_facilitator_about_value = models.TextField(blank=True)
    field_course_facilitator_about_format = models.IntegerField(null=True, blank=True)
    field_course_photo_fid = models.IntegerField(null=True, blank=True)
    field_course_photo_list = models.IntegerField(null=True, blank=True)
    field_course_photo_data = models.TextField(blank=True)
    field_course_short_desc_value = models.CharField(max_length=420, blank=True)
    field_refers_to_syllabus_nid = models.IntegerField(null=True, blank=True)
    field_course_summary_value = models.TextField(blank=True)
    field_course_summary_format = models.IntegerField(null=True, blank=True)
    field_course_prerequisites_value = models.TextField(blank=True)
    field_course_prerequisites_format = models.IntegerField(null=True, blank=True)
    field_course_sign_up_req_value = models.TextField(blank=True)
    field_course_sign_up_req_format = models.IntegerField(null=True, blank=True)
    field_course_no_of_seats_value = models.IntegerField(null=True, blank=True)
    field_course_learning_objectives_value = models.TextField(blank=True)
    field_course_learning_objectives_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_course'

class ContentTypeCourseApplication(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_application_motivation_value = models.TextField(blank=True)
    field_application_background_value = models.TextField(blank=True)
    field_application_applicant_uid = models.IntegerField(null=True, blank=True)
    field_application_assignme_value = models.TextField(blank=True)
    field_application_background_format = models.IntegerField(null=True, blank=True)
    field_application_motivation_format = models.IntegerField(null=True, blank=True)
    field_application_assignme_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_course_application'

class ContentTypeDocument(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_document_body_value = models.TextField(blank=True)
    field_document_body_format = models.IntegerField(null=True, blank=True)
    field_document_order_value = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_document'

class ContentTypeEvent(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_event_date_value = models.DateTimeField(null=True, blank=True)
    field_event_date_value2 = models.DateTimeField(null=True, blank=True)
    field_event_detail_value = models.TextField(blank=True)
    field_event_detail_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_event'

class ContentTypeProfile(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_profile_country_value = models.TextField(blank=True)
    field_profile_city_value = models.TextField(blank=True)
    field_profile_aboutme_value = models.TextField(blank=True)
    field_profile_aboutme_format = models.IntegerField(null=True, blank=True)
    field_profile_firstname_value = models.TextField(blank=True)
    field_profile_lastname_value = models.TextField(blank=True)
    field_profile_facebook_url = models.CharField(max_length=765, blank=True)
    field_profile_facebook_title = models.CharField(max_length=765, blank=True)
    field_profile_facebook_attributes = models.TextField(blank=True)
    field_profile_twitter_url = models.CharField(max_length=765, blank=True)
    field_profile_twitter_title = models.CharField(max_length=765, blank=True)
    field_profile_twitter_attributes = models.TextField(blank=True)
    field_profile_gender_value = models.TextField(blank=True)
    field_profile_education_value = models.TextField(blank=True)
    field_profile_email_subs_value = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_profile'

class ContentTypeRecommendation(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_recommendation_value = models.TextField(blank=True)
    field_recommendation_user_uid = models.IntegerField(null=True, blank=True)
    field_recommendation_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_recommendation'

class ContentTypeReportCard(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_report_card_user_uid = models.IntegerField(null=True, blank=True)
    field_report_card_result_value = models.TextField(blank=True)
    class Meta:
        db_table = u'content_type_report_card'

class ContentTypeShoutBox(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_shoutbox_shout_value = models.TextField(blank=True)
    class Meta:
        db_table = u'content_type_shout_box'

class ContentTypeSiteNews(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_site_news_body_value = models.TextField(blank=True)
    field_site_news_body_format = models.IntegerField(null=True, blank=True)
    field_site_news_main_image_fid = models.IntegerField(null=True, blank=True)
    field_site_news_main_image_list = models.IntegerField(null=True, blank=True)
    field_site_news_main_image_data = models.TextField(blank=True)
    class Meta:
        db_table = u'content_type_site_news'

class ContentTypeSubmission(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_submission_assignment_nid = models.IntegerField(null=True, blank=True)
    field_submission_status_value = models.TextField(blank=True)
    field_submission_content_value = models.TextField(blank=True)
    field_submission_content_format = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'content_type_submission'

class ContentTypeTeamMember(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_team_member_body_value = models.TextField(blank=True)
    field_team_member_body_format = models.IntegerField(null=True, blank=True)
    field_team_member_main_image_fid = models.IntegerField(null=True, blank=True)
    field_team_member_main_image_list = models.IntegerField(null=True, blank=True)
    field_team_member_main_image_data = models.TextField(blank=True)
    field_team_member_type_value = models.TextField(blank=True)
    class Meta:
        db_table = u'content_type_team_member'

class Context(models.Model):
    name = models.CharField(max_length=765, primary_key=True)
    description = models.CharField(max_length=765)
    tag = models.CharField(max_length=765)
    conditions = models.TextField(blank=True)
    reactions = models.TextField(blank=True)
    condition_mode = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'context'

class CtoolsCssCache(models.Model):
    cid = models.CharField(max_length=384, primary_key=True)
    filename = models.CharField(max_length=765, blank=True)
    css = models.TextField(blank=True)
    filter = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ctools_css_cache'

class CtoolsObjectCache(models.Model):
    sid = models.CharField(max_length=192, primary_key=True)
    name = models.CharField(max_length=384, primary_key=True)
    obj = models.CharField(max_length=96, primary_key=True)
    updated = models.IntegerField()
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'ctools_object_cache'

class DateFormatLocale(models.Model):
    format = models.CharField(max_length=300)
    type = models.CharField(max_length=600, primary_key=True)
    language = models.CharField(max_length=36, primary_key=True)
    class Meta:
        db_table = u'date_format_locale'

class DateFormatTypes(models.Model):
    type = models.CharField(max_length=600, primary_key=True)
    title = models.CharField(max_length=765)
    locked = models.IntegerField()
    class Meta:
        db_table = u'date_format_types'

class DateFormats(models.Model):
    dfid = models.IntegerField(primary_key=True)
    format = models.CharField(unique=True, max_length=300)
    type = models.CharField(unique=True, max_length=600)
    locked = models.IntegerField()
    class Meta:
        db_table = u'date_formats'

class DevelQueries(models.Model):
    qid = models.IntegerField()
    function = models.CharField(max_length=765)
    query = models.TextField()
    hash = models.CharField(max_length=765, primary_key=True)
    class Meta:
        db_table = u'devel_queries'

class DevelTimes(models.Model):
    tid = models.IntegerField(primary_key=True)
    qid = models.IntegerField()
    time = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'devel_times'

class FaqQuestions(models.Model):
    nid = models.IntegerField(primary_key=True)
    vid = models.IntegerField(primary_key=True)
    question = models.TextField()
    detailed_question = models.TextField()
    class Meta:
        db_table = u'faq_questions'

class FaqWeights(models.Model):
    tid = models.IntegerField(primary_key=True)
    nid = models.IntegerField(primary_key=True)
    weight = models.IntegerField()
    class Meta:
        db_table = u'faq_weights'

class FckeditorRole(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    rid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'fckeditor_role'

class FckeditorSettings(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'fckeditor_settings'

class FilefieldMeta(models.Model):
    fid = models.IntegerField(primary_key=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    audio_format = models.CharField(max_length=30)
    audio_sample_rate = models.IntegerField()
    audio_channel_mode = models.CharField(max_length=30)
    audio_bitrate = models.FloatField()
    audio_bitrate_mode = models.CharField(max_length=12)
    tags = models.TextField(blank=True)
    class Meta:
        db_table = u'filefield_meta'

class FilefieldPaths(models.Model):
    type = models.CharField(unique=True, max_length=96)
    field = models.CharField(unique=True, max_length=96)
    filename = models.TextField()
    filepath = models.TextField()
    class Meta:
        db_table = u'filefield_paths'

class Files(models.Model):
    fid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    filename = models.CharField(max_length=765)
    filepath = models.CharField(max_length=765)
    filemime = models.CharField(max_length=765)
    filesize = models.IntegerField()
    status = models.IntegerField()
    timestamp = models.IntegerField()
    origname = models.CharField(max_length=765)
    class Meta:
        db_table = u'files'

class FilterFormats(models.Model):
    format = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765)
    roles = models.CharField(max_length=765)
    cache = models.IntegerField()
    class Meta:
        db_table = u'filter_formats'

class Filters(models.Model):
    fid = models.IntegerField(primary_key=True)
    format = models.IntegerField()
    module = models.CharField(max_length=192)
    delta = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'filters'

class FlagContent(models.Model):
    fcid = models.IntegerField(primary_key=True)
    fid = models.IntegerField(unique=True)
    content_type = models.CharField(max_length=96)
    content_id = models.IntegerField()
    uid = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'flag_content'

class FlagCounts(models.Model):
    fid = models.IntegerField()
    content_type = models.CharField(max_length=96)
    content_id = models.IntegerField()
    count = models.IntegerField()
    class Meta:
        db_table = u'flag_counts'

class FlagTypes(models.Model):
    fid = models.IntegerField()
    type = models.CharField(max_length=96)
    class Meta:
        db_table = u'flag_types'

class Flags(models.Model):
    fid = models.IntegerField(primary_key=True)
    content_type = models.CharField(max_length=96)
    name = models.CharField(unique=True, max_length=96, blank=True)
    title = models.CharField(max_length=765, blank=True)
    roles = models.CharField(max_length=765, blank=True)
    global_field = models.IntegerField(null=True, db_column='global', blank=True) # Field renamed because it was a Python reserved word. Field name made lowercase.
    options = models.TextField(blank=True)
    class Meta:
        db_table = u'flags'

class Flood(models.Model):
    fid = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=192)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'flood'

class FormdefaultsForms(models.Model):
    formid = models.CharField(max_length=765, primary_key=True)
    formdata = models.TextField(blank=True)
    class Meta:
        db_table = u'formdefaults_forms'

class Forum(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    tid = models.IntegerField()
    class Meta:
        db_table = u'forum'

class FuploadPreviewlist(models.Model):
    fieldname = models.CharField(max_length=96)
    uid = models.IntegerField()
    nid = models.IntegerField()
    fid = models.IntegerField(primary_key=True)
    created = models.IntegerField()
    class Meta:
        db_table = u'fupload_previewlist'

class History(models.Model):
    uid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'history'

class Image(models.Model):
    nid = models.IntegerField(primary_key=True)
    fid = models.IntegerField()
    image_size = models.CharField(max_length=96, primary_key=True)
    class Meta:
        db_table = u'image'

class ImagecacheAction(models.Model):
    actionid = models.IntegerField(primary_key=True)
    presetid = models.IntegerField()
    weight = models.IntegerField()
    module = models.CharField(max_length=765)
    action = models.CharField(max_length=765)
    data = models.TextField()
    class Meta:
        db_table = u'imagecache_action'

class ImagecachePreset(models.Model):
    presetid = models.IntegerField(primary_key=True)
    presetname = models.CharField(max_length=765)
    class Meta:
        db_table = u'imagecache_preset'

class Languages(models.Model):
    language = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=192)
    native = models.CharField(max_length=192)
    direction = models.IntegerField()
    enabled = models.IntegerField()
    plurals = models.IntegerField()
    formula = models.CharField(max_length=384)
    domain = models.CharField(max_length=384)
    prefix = models.CharField(max_length=384)
    weight = models.IntegerField()
    javascript = models.CharField(max_length=96)
    class Meta:
        db_table = u'languages'

class LocalesSource(models.Model):
    lid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=765)
    textgroup = models.CharField(max_length=765)
    source = models.TextField()
    version = models.CharField(max_length=60)
    class Meta:
        db_table = u'locales_source'

class LocalesTarget(models.Model):
    lid = models.IntegerField()
    translation = models.TextField()
    language = models.CharField(max_length=36, primary_key=True)
    plid = models.IntegerField()
    plural = models.IntegerField()
    class Meta:
        db_table = u'locales_target'

class Masquerade(models.Model):
    sid = models.CharField(max_length=192)
    uid_from = models.IntegerField()
    uid_as = models.IntegerField()
    class Meta:
        db_table = u'masquerade'

class MasqueradeUsers(models.Model):
    uid_from = models.IntegerField(primary_key=True)
    uid_to = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'masquerade_users'

class MassContact(models.Model):
    cid = models.IntegerField(primary_key=True)
    category = models.CharField(unique=True, max_length=765)
    recipients = models.TextField()
    reply = models.TextField()
    weight = models.IntegerField()
    selected = models.IntegerField()
    class Meta:
        db_table = u'mass_contact'

class MenuCustom(models.Model):
    menu_name = models.CharField(max_length=96, primary_key=True)
    title = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'menu_custom'

class MenuLinks(models.Model):
    menu_name = models.CharField(max_length=96)
    mlid = models.IntegerField(primary_key=True)
    plid = models.IntegerField()
    link_path = models.CharField(max_length=765)
    router_path = models.CharField(max_length=765)
    link_title = models.CharField(max_length=765)
    options = models.TextField(blank=True)
    module = models.CharField(max_length=765)
    hidden = models.IntegerField()
    external = models.IntegerField()
    has_children = models.IntegerField()
    expanded = models.IntegerField()
    weight = models.IntegerField()
    depth = models.IntegerField()
    customized = models.IntegerField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    updated = models.IntegerField()
    class Meta:
        db_table = u'menu_links'

class MenuPerRole(models.Model):
    mlid = models.IntegerField(primary_key=True)
    rids = models.TextField()
    hrids = models.TextField()
    class Meta:
        db_table = u'menu_per_role'

class MenuRouter(models.Model):
    path = models.CharField(max_length=765, primary_key=True)
    load_functions = models.TextField()
    to_arg_functions = models.TextField()
    access_callback = models.CharField(max_length=765)
    access_arguments = models.TextField(blank=True)
    page_callback = models.CharField(max_length=765)
    page_arguments = models.TextField(blank=True)
    fit = models.IntegerField()
    number_parts = models.IntegerField()
    tab_parent = models.CharField(max_length=765)
    tab_root = models.CharField(max_length=765)
    title = models.CharField(max_length=765)
    title_callback = models.CharField(max_length=765)
    title_arguments = models.CharField(max_length=765)
    type = models.IntegerField()
    block_callback = models.CharField(max_length=765)
    description = models.TextField()
    position = models.CharField(max_length=765)
    weight = models.IntegerField()
    file = models.TextField(blank=True)
    class Meta:
        db_table = u'menu_router'

class MessagingMessageParts(models.Model):
    type = models.CharField(max_length=300)
    method = models.CharField(max_length=150)
    msgkey = models.CharField(max_length=300)
    module = models.CharField(max_length=765)
    message = models.TextField()
    class Meta:
        db_table = u'messaging_message_parts'

class MessagingStore(models.Model):
    mqid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    sender = models.IntegerField()
    method = models.CharField(max_length=765)
    destination = models.CharField(max_length=765)
    subject = models.CharField(max_length=765)
    body = models.TextField()
    params = models.TextField()
    created = models.IntegerField()
    sent = models.IntegerField()
    cron = models.IntegerField()
    queue = models.IntegerField()
    log = models.IntegerField()
    class Meta:
        db_table = u'messaging_store'

class Mollom(models.Model):
    entity = models.CharField(max_length=96, primary_key=True)
    did = models.CharField(max_length=96, primary_key=True)
    session = models.CharField(max_length=765)
    changed = models.IntegerField()
    quality = models.FloatField(null=True, blank=True)
    languages = models.CharField(max_length=765)
    spam = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'mollom'

class MollomForm(models.Model):
    form_id = models.CharField(max_length=765, primary_key=True)
    mode = models.IntegerField()
    enabled_fields = models.TextField(blank=True)
    module = models.CharField(max_length=765)
    checks = models.TextField(blank=True)
    class Meta:
        db_table = u'mollom_form'

class Node(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField(unique=True)
    type = models.CharField(max_length=96)
    language = models.CharField(max_length=36)
    title = models.CharField(max_length=765)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()
    comment = models.IntegerField()
    promote = models.IntegerField()
    moderate = models.IntegerField()
    sticky = models.IntegerField()
    tnid = models.IntegerField()
    translate = models.IntegerField()
    class Meta:
        db_table = u'node'

class NodeAccess(models.Model):
    nid = models.IntegerField(primary_key=True)
    gid = models.IntegerField(primary_key=True)
    realm = models.CharField(max_length=765, primary_key=True)
    grant_view = models.IntegerField()
    grant_update = models.IntegerField()
    grant_delete = models.IntegerField()
    class Meta:
        db_table = u'node_access'

class NodeCommentStatistics(models.Model):
    nid = models.IntegerField(primary_key=True)
    last_comment_timestamp = models.IntegerField()
    last_comment_name = models.CharField(max_length=180, blank=True)
    last_comment_uid = models.IntegerField()
    comment_count = models.IntegerField()
    class Meta:
        db_table = u'node_comment_statistics'

class NodeConvertTemplates(models.Model):
    nctid = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    source_type = models.TextField(blank=True)
    destination_type = models.TextField()
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'node_convert_templates'

class NodeCounter(models.Model):
    nid = models.IntegerField(primary_key=True)
    totalcount = models.BigIntegerField()
    daycount = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'node_counter'

class NodeRevisions(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    title = models.CharField(max_length=765)
    body = models.TextField()
    teaser = models.TextField()
    log = models.TextField()
    timestamp = models.IntegerField()
    format = models.IntegerField()
    class Meta:
        db_table = u'node_revisions'

class NodeType(models.Model):
    type = models.CharField(max_length=96, primary_key=True)
    name = models.CharField(max_length=765)
    module = models.CharField(max_length=765)
    description = models.TextField()
    help = models.TextField()
    has_title = models.IntegerField()
    title_label = models.CharField(max_length=765)
    has_body = models.IntegerField()
    body_label = models.CharField(max_length=765)
    min_word_count = models.IntegerField()
    custom = models.IntegerField()
    modified = models.IntegerField()
    locked = models.IntegerField()
    orig_type = models.CharField(max_length=765)
    class Meta:
        db_table = u'node_type'

class Notifications(models.Model):
    sid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    type = models.CharField(max_length=765, blank=True)
    event_type = models.CharField(max_length=765, blank=True)
    conditions = models.IntegerField()
    send_interval = models.IntegerField(null=True, blank=True)
    send_method = models.CharField(max_length=765)
    cron = models.IntegerField()
    module = models.CharField(max_length=765, blank=True)
    status = models.IntegerField()
    destination = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'notifications'

class NotificationsEvent(models.Model):
    eid = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=765, blank=True)
    action = models.CharField(max_length=765, blank=True)
    oid = models.IntegerField()
    language = models.CharField(max_length=765, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    params = models.TextField(blank=True)
    created = models.IntegerField()
    counter = models.IntegerField()
    class Meta:
        db_table = u'notifications_event'

class NotificationsFields(models.Model):
    sid = models.IntegerField(primary_key=True)
    field = models.CharField(max_length=765, primary_key=True)
    value = models.CharField(max_length=765)
    intval = models.IntegerField()
    class Meta:
        db_table = u'notifications_fields'

class NotificationsQueue(models.Model):
    sqid = models.IntegerField(primary_key=True)
    eid = models.IntegerField()
    sid = models.IntegerField()
    uid = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=765, blank=True)
    send_interval = models.IntegerField(null=True, blank=True)
    send_method = models.CharField(max_length=765, blank=True)
    sent = models.IntegerField()
    created = models.IntegerField()
    cron = models.IntegerField()
    conditions = models.IntegerField()
    module = models.CharField(max_length=765, blank=True)
    destination = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'notifications_queue'

class NotificationsSent(models.Model):
    uid = models.IntegerField(primary_key=True)
    send_interval = models.IntegerField(primary_key=True)
    send_method = models.CharField(max_length=150, primary_key=True)
    sent = models.IntegerField()
    class Meta:
        db_table = u'notifications_sent'

class Og(models.Model):
    nid = models.IntegerField(primary_key=True)
    og_selective = models.IntegerField()
    og_description = models.CharField(max_length=765, blank=True)
    og_theme = models.CharField(max_length=765, blank=True)
    og_register = models.IntegerField()
    og_directory = models.IntegerField()
    og_language = models.CharField(max_length=36)
    og_private = models.IntegerField()
    class Meta:
        db_table = u'og'

class OgAccessPost(models.Model):
    nid = models.IntegerField(primary_key=True)
    og_public = models.IntegerField()
    class Meta:
        db_table = u'og_access_post'

class OgAncestry(models.Model):
    nid = models.IntegerField(primary_key=True)
    group_nid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'og_ancestry'

class OgNotifications(models.Model):
    uid = models.IntegerField(primary_key=True)
    autosubscribe = models.IntegerField()
    class Meta:
        db_table = u'og_notifications'

class OgTerm(models.Model):
    tid = models.IntegerField(primary_key=True)
    nid = models.IntegerField(primary_key=True)
    public = models.IntegerField()
    class Meta:
        db_table = u'og_term'

class OgUid(models.Model):
    nid = models.IntegerField(primary_key=True)
    og_role = models.IntegerField()
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    uid = models.IntegerField(primary_key=True)
    created = models.IntegerField(null=True, blank=True)
    changed = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'og_uid'

class OpenidAssociation(models.Model):
    idp_endpoint_uri = models.CharField(max_length=765, blank=True)
    assoc_handle = models.CharField(max_length=765, primary_key=True)
    assoc_type = models.CharField(max_length=96, blank=True)
    session_type = models.CharField(max_length=96, blank=True)
    mac_key = models.CharField(max_length=765, blank=True)
    created = models.IntegerField()
    expires_in = models.IntegerField()
    class Meta:
        db_table = u'openid_association'

class OpenidNonce(models.Model):
    idp_endpoint_uri = models.CharField(max_length=765, blank=True)
    nonce = models.CharField(max_length=765, blank=True)
    expires = models.IntegerField()
    class Meta:
        db_table = u'openid_nonce'

class P2PuStatsAccesslog(models.Model):
    rid = models.IntegerField(primary_key=True)
    aid = models.IntegerField()
    sid = models.CharField(max_length=192)
    title = models.CharField(max_length=765, blank=True)
    path = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    hostname = models.CharField(max_length=384, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    timer = models.IntegerField()
    timestamp = models.IntegerField()
    action = models.CharField(max_length=765)
    course_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'p2pu_stats_accesslog'

class PageManagerHandlers(models.Model):
    did = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765, blank=True)
    task = models.CharField(max_length=192, blank=True)
    subtask = models.CharField(max_length=192)
    handler = models.CharField(max_length=192, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    conf = models.TextField()
    class Meta:
        db_table = u'page_manager_handlers'

class PageManagerPages(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765, blank=True)
    task = models.CharField(max_length=192, blank=True)
    admin_title = models.CharField(max_length=765, blank=True)
    admin_description = models.TextField(blank=True)
    path = models.CharField(max_length=765, blank=True)
    access = models.TextField()
    menu = models.TextField()
    arguments = models.TextField()
    conf = models.TextField()
    class Meta:
        db_table = u'page_manager_pages'

class PageManagerWeights(models.Model):
    name = models.CharField(max_length=765)
    weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'page_manager_weights'

class PanelsDisplay(models.Model):
    did = models.IntegerField(primary_key=True)
    layout = models.CharField(max_length=96, blank=True)
    layout_settings = models.TextField(blank=True)
    panel_settings = models.TextField(blank=True)
    cache = models.TextField(blank=True)
    title = models.CharField(max_length=765, blank=True)
    hide_title = models.IntegerField(null=True, blank=True)
    title_pane = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'panels_display'

class PanelsLayout(models.Model):
    lid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    admin_title = models.CharField(max_length=765, blank=True)
    admin_description = models.TextField(blank=True)
    category = models.CharField(max_length=765, blank=True)
    plugin = models.CharField(max_length=765, blank=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'panels_layout'

class PanelsMini(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765, blank=True)
    category = models.CharField(max_length=192, blank=True)
    did = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=384, blank=True)
    requiredcontexts = models.TextField(blank=True)
    contexts = models.TextField(blank=True)
    relationships = models.TextField(blank=True)
    admin_description = models.TextField(blank=True)
    class Meta:
        db_table = u'panels_mini'

class PanelsPane(models.Model):
    pid = models.IntegerField(primary_key=True)
    did = models.IntegerField()
    panel = models.CharField(max_length=96, blank=True)
    type = models.CharField(max_length=96, blank=True)
    subtype = models.CharField(max_length=192, blank=True)
    shown = models.IntegerField(null=True, blank=True)
    access = models.TextField(blank=True)
    configuration = models.TextField(blank=True)
    cache = models.TextField(blank=True)
    style = models.TextField(blank=True)
    css = models.TextField(blank=True)
    extras = models.TextField(blank=True)
    position = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'panels_pane'

class PanelsRendererPipeline(models.Model):
    rpid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    admin_title = models.CharField(max_length=765, blank=True)
    admin_description = models.TextField(blank=True)
    weight = models.IntegerField(null=True, blank=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'panels_renderer_pipeline'

class PathRedirect(models.Model):
    rid = models.IntegerField(primary_key=True)
    source = models.CharField(unique=True, max_length=765)
    redirect = models.CharField(max_length=765)
    query = models.CharField(max_length=765, blank=True)
    fragment = models.CharField(max_length=150, blank=True)
    language = models.CharField(unique=True, max_length=36)
    type = models.IntegerField()
    last_used = models.IntegerField()
    class Meta:
        db_table = u'path_redirect'

class Permission(models.Model):
    pid = models.IntegerField(primary_key=True)
    rid = models.IntegerField()
    perm = models.TextField(blank=True)
    tid = models.IntegerField()
    class Meta:
        db_table = u'permission'

class ProfileFields(models.Model):
    fid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765, blank=True)
    name = models.CharField(unique=True, max_length=384)
    explanation = models.TextField(blank=True)
    category = models.CharField(max_length=765, blank=True)
    page = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=384, blank=True)
    weight = models.IntegerField()
    required = models.IntegerField()
    register = models.IntegerField()
    visibility = models.IntegerField()
    autocomplete = models.IntegerField()
    options = models.TextField(blank=True)
    class Meta:
        db_table = u'profile_fields'

class ProfilePrivacyFields(models.Model):
    fid = models.IntegerField(primary_key=True)
    privacy = models.IntegerField()
    class Meta:
        db_table = u'profile_privacy_fields'

class ProfilePrivacyValues(models.Model):
    fid = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    private = models.IntegerField()
    class Meta:
        db_table = u'profile_privacy_values'

class ProfileValues(models.Model):
    fid = models.IntegerField()
    uid = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = u'profile_values'

class Purl(models.Model):
    value = models.CharField(max_length=765, primary_key=True)
    provider = models.CharField(max_length=765)
    id = models.IntegerField()
    class Meta:
        db_table = u'purl'

class Realname(models.Model):
    uid = models.IntegerField(primary_key=True)
    realname = models.CharField(max_length=765)
    class Meta:
        db_table = u'realname'

class Role(models.Model):
    rid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=192)
    class Meta:
        db_table = u'role'

class RulesRules(models.Model):
    name = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'rules_rules'

class RulesSets(models.Model):
    name = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'rules_sets'

class SearchDataset(models.Model):
    sid = models.IntegerField(unique=True)
    type = models.CharField(unique=True, max_length=48, blank=True)
    data = models.TextField()
    reindex = models.IntegerField()
    class Meta:
        db_table = u'search_dataset'

class SearchIndex(models.Model):
    word = models.CharField(max_length=150)
    sid = models.IntegerField()
    type = models.CharField(max_length=48, blank=True)
    score = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'search_index'

class SearchNodeLinks(models.Model):
    sid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=48, primary_key=True)
    nid = models.IntegerField()
    caption = models.TextField(blank=True)
    class Meta:
        db_table = u'search_node_links'

class SearchTotal(models.Model):
    word = models.CharField(max_length=150, primary_key=True)
    count = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'search_total'

class Semaphore(models.Model):
    name = models.CharField(max_length=765, primary_key=True)
    value = models.CharField(max_length=765)
    expire = models.FloatField()
    class Meta:
        db_table = u'semaphore'

class Sessions(models.Model):
    uid = models.IntegerField()
    sid = models.CharField(max_length=192, primary_key=True)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    cache = models.IntegerField()
    session = models.TextField(blank=True)
    class Meta:
        db_table = u'sessions'

class Statspro(models.Model):
    day = models.IntegerField(primary_key=True)
    nuser = models.IntegerField()
    auser = models.IntegerField()
    nnode = models.IntegerField()
    cnode = models.IntegerField()
    comment = models.IntegerField()
    pi = models.IntegerField()
    upi = models.IntegerField()
    error = models.IntegerField()
    uerror = models.IntegerField()
    warning = models.IntegerField()
    uwarning = models.IntegerField()
    class Meta:
        db_table = u'statspro'

class StatsproTerm(models.Model):
    tid = models.IntegerField(primary_key=True)
    ncount = models.IntegerField()
    class Meta:
        db_table = u'statspro_term'

class Stylizer(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765, blank=True)
    admin_title = models.CharField(max_length=765, blank=True)
    admin_description = models.TextField(blank=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'stylizer'

class System(models.Model):
    filename = models.CharField(max_length=765)
    name = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    owner = models.CharField(max_length=765)
    status = models.IntegerField()
    throttle = models.IntegerField()
    bootstrap = models.IntegerField()
    schema_version = models.IntegerField()
    weight = models.IntegerField()
    info = models.TextField(blank=True)
    class Meta:
        db_table = u'system'

class TermData(models.Model):
    tid = models.IntegerField(primary_key=True)
    vid = models.IntegerField()
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    weight = models.IntegerField()
    class Meta:
        db_table = u'term_data'

class TermHierarchy(models.Model):
    tid = models.IntegerField(primary_key=True)
    parent = models.IntegerField()
    class Meta:
        db_table = u'term_hierarchy'

class TermNode(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField()
    tid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'term_node'

class TermRelation(models.Model):
    trid = models.IntegerField(primary_key=True)
    tid1 = models.IntegerField(unique=True)
    tid2 = models.IntegerField()
    class Meta:
        db_table = u'term_relation'

class TermSynonym(models.Model):
    tsid = models.IntegerField(primary_key=True)
    tid = models.IntegerField()
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'term_synonym'

class Upload(models.Model):
    fid = models.IntegerField()
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=765)
    list = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'upload'

class UrlAlias(models.Model):
    pid = models.IntegerField()
    src = models.CharField(max_length=384)
    dst = models.CharField(unique=True, max_length=768, blank=True)
    language = models.CharField(max_length=36)
    class Meta:
        db_table = u'url_alias'

class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=180)
    pass_field = models.CharField(max_length=96, db_column='pass') # Field renamed because it was a Python reserved word. Field name made lowercase.
    mail = models.CharField(max_length=192, blank=True)
    mode = models.IntegerField()
    sort = models.IntegerField(null=True, blank=True)
    threshold = models.IntegerField(null=True, blank=True)
    theme = models.CharField(max_length=765)
    signature = models.CharField(max_length=765)
    signature_format = models.IntegerField()
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=24, blank=True)
    language = models.CharField(max_length=36)
    picture = models.CharField(max_length=765)
    init = models.CharField(max_length=192, blank=True)
    data = models.TextField(blank=True)
    timezone_name = models.CharField(max_length=150)
    class Meta:
        db_table = u'users'

class UsersRoles(models.Model):
    uid = models.IntegerField(primary_key=True)
    rid = models.IntegerField()
    class Meta:
        db_table = u'users_roles'

class Variable(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    value = models.TextField()
    class Meta:
        db_table = u'variable'

class Viewreference(models.Model):
    view_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=96)
    position = models.CharField(max_length=192)
    title = models.CharField(max_length=765)
    class Meta:
        db_table = u'viewreference'

class ViewsDisplay(models.Model):
    vid = models.IntegerField()
    id = models.CharField(max_length=192, primary_key=True)
    display_title = models.CharField(max_length=192)
    display_plugin = models.CharField(max_length=192)
    position = models.IntegerField(null=True, blank=True)
    display_options = models.TextField(blank=True)
    class Meta:
        db_table = u'views_display'

class ViewsObjectCache(models.Model):
    sid = models.CharField(max_length=192, blank=True)
    name = models.CharField(max_length=96, blank=True)
    obj = models.CharField(max_length=96, blank=True)
    updated = models.IntegerField()
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'views_object_cache'

class ViewsView(models.Model):
    vid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=96)
    description = models.CharField(max_length=765, blank=True)
    tag = models.CharField(max_length=765, blank=True)
    view_php = models.TextField(blank=True)
    base_table = models.CharField(max_length=192)
    is_cacheable = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'views_view'

class Vocabulary(models.Model):
    vid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    help = models.CharField(max_length=765)
    relations = models.IntegerField()
    hierarchy = models.IntegerField()
    multiple = models.IntegerField()
    required = models.IntegerField()
    tags = models.IntegerField()
    module = models.CharField(max_length=765)
    weight = models.IntegerField()
    class Meta:
        db_table = u'vocabulary'

class VocabularyNodeTypes(models.Model):
    vid = models.IntegerField()
    type = models.CharField(max_length=96, primary_key=True)
    class Meta:
        db_table = u'vocabulary_node_types'

class Watchdog(models.Model):
    wid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    type = models.CharField(max_length=48)
    message = models.TextField()
    variables = models.TextField()
    severity = models.IntegerField()
    link = models.CharField(max_length=765)
    location = models.TextField()
    referer = models.TextField(blank=True)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'watchdog'

