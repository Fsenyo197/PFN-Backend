from blog.models.category_model import Category

class CategoryRepository:
    def get_all_categories(self):
        return Category.objects.all()
