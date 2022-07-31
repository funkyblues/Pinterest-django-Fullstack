from django.contrib.auth.forms import UserCreationForm

# UserCreationForm을 상속받아서 사용자가 아이디는 변경할 수 없도록.
# 그러나 비활 되어 있더라고 클라이언트에서 변경되어서 올 수도 있다. 그러니까 서버는 무조건 믿으면 안되는 거임
# 아이디를 바꿔도 원래 아이디의 비밀번호가 변경된 것으로 DB에 저장된다
class AccountUpdateForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['username'].disabled = True