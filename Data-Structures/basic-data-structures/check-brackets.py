def are_matching(left: str, right: str) -> bool:
  return left+right in ['[]', '{}', '()']


def isBalanced(string: str) -> bool:
  stack = []
  mapping = {
    '[': ']',
    '{': '}',
    '(': ')'
  }

  for char in string:
    if char in ['[', '{', '(']:
      stack.append(char)
    elif char in [']', '}', ')']:
      if mapping[stack[-1]] == char:
        stack.pop()
      else:
        return False

  return not bool(stack)

print(isBalanced('foo(bar[i]);'))

