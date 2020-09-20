from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from post.models import Category, Post, Images, Comment


class PostImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category',  'image_tag','catimg_tag' ,'status']
    readonly_fields = ('image_tag','catimg_tag')
    list_filter = ['status', 'category']
    inlines = [PostImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image_tag']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_posts_count', 'related_posts_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Post,
            'category',
            'posts_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Post,
                                                'category',
                                                'posts_count',
                                                cumulative=False)
        return qs

    def related_posts_count(self, instance):
        return instance.posts_count

    related_posts_count.short_description = 'Related posts (for this specific category)'

    def related_posts_cumulative_count(self, instance):
        return instance.posts_cumulative_count

    related_posts_cumulative_count.short_description = 'Related posts (in tree)'

class commentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','post','user','status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment,commentAdmin)