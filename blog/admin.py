from django.contrib import admin
from .models import Post, Category #nome da classe q vc colocou
# Register your models here.


@admin.register(Category)   #para mostrar a class criada no models no painel admi
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome',  'criado', 'publicado') #quais dados vc quer exibir
    list_filter = ('nome',  'criado', 'publicado') #criar filtro lateral por publicado ou rascunho, data de criação, data de publicacao e autor
    date_hierarchy = 'publicado' #criar ordenagem por data de postagem
    search_fields = ('nome',) #adicionar caixa de texto e filtrar por titulo e conteudo
    
    
@admin.register(Post)   #para mostrar a class criada no models no painel admi
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo',  'autor', 'publicado', 'status') #quais dados vc quer exibir
    list_filter = ('status', 'criado', 'publicado', 'autor',) #criar filtro lateral por publicado ou rascunho, data de criação, data de publicacao e autor
    readonly_fields = ('visualizar_imagem',)
    raw_id_fields = ('autor',) #criação a partir do id do admin, foreign key
    date_hierarchy = 'publicado' #criar ordenagem por data de postagem
    search_fields = ('titulo', 'conteudo') #adicionar caixa de texto e filtrar por titulo e conteudo
    prepopulated_fields = {'slug': ('titulo',)} #para que um valor se iguale ao outro
    
    def visualizar_imagem(self,obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada"

