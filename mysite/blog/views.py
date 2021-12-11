from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
##############################
##############################



















####################################
###################################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        from = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=Fasle)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'from':form})
