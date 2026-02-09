from django.contrib.auth.models import User
from django.views.generic import DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from followers.models import Follower
from feed.models import Post
from .forms import UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm


class ProfileDetail(DetailView):
    http_method_names = ['get']
    template_name = 'profiles/detail.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        total_posts = Post.objects.filter(author=user).count()
        total_followers = Follower.objects.filter(following=user).count()
        total_following = Follower.objects.filter(followed_by=user).count()
        context['total_posts'] = total_posts
        context['total_followers'] = total_followers
        context['total_following'] = total_following
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(
                followed_by=self.request.user,
                following=user
            ).exists()

        return context


class FollowView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            other_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("User does not exist")

        if data['action'] == 'follow':
            # Follow
            follower, created = Follower.objects.get_or_create(
                followed_by=request.user,
                following=other_user
            )
        else:
            # Unfollow
            Follower.objects.filter(
                followed_by=request.user,
                following=other_user
            ).delete()

        return JsonResponse({'success': True, 'wording': "Unfollow" if data['action'] == 'follow' else "Follow"})


class ProfileEditView(LoginRequiredMixin, View):
    http_method_names = ['get', 'post']
    template_name = 'profiles/edit.html'

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)

        # Only allow users to edit their own profile
        if request.user != user:
            messages.error(request, "You can only edit your own profile.")
            return redirect('profiles:detail', username=username)

        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)
        password_form = CustomPasswordChangeForm(user=user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'password_form': password_form,
            'profile_user': user,
        }

        return self.render_to_response(context)

    def post(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)

        # Only allow users to edit their own profile
        if request.user != user:
            messages.error(request, "You can only edit your own profile.")
            return redirect('profiles:detail', username=username)

        form_type = request.POST.get('form_type')

        if form_type == 'profile':
            user_form = UserUpdateForm(request.POST, instance=user)
            profile_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(
                    request, "Your profile has been updated successfully!")
                return redirect('profiles:edit', username=user.username)
            else:
                password_form = CustomPasswordChangeForm(user=user)

        elif form_type == 'password':
            password_form = CustomPasswordChangeForm(
                user=user, data=request.POST)

            if password_form.is_valid():
                password_form.save()
                messages.success(
                    request, "Your password has been changed successfully!")
                return redirect('profiles:edit', username=username)
            else:
                user_form = UserUpdateForm(instance=user)
                profile_form = ProfileUpdateForm(instance=user.profile)
        else:
            user_form = UserUpdateForm(instance=user)
            profile_form = ProfileUpdateForm(instance=user.profile)
            password_form = CustomPasswordChangeForm(user=user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'password_form': password_form,
            'profile_user': user,
        }

        return self.render_to_response(context)

    def render_to_response(self, context):
        from django.shortcuts import render
        return render(self.request, self.template_name, context)
