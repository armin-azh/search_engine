from collections import deque
from utils import intersect, union, not_operator


class Search(object):
    AND_TOKEN = 'AND'
    OR_TOKEN = 'OR'
    NOT_TOKEN = 'NOT'
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'

    def __init__(self):
        pass

    def _postfix(self, infix_token):

        precedence = dict()
        precedence[self.NOT_TOKEN] = 3
        precedence[self.AND_TOKEN] = 2
        precedence[self.OR_TOKEN] = 1
        precedence[self.LEFT_BRACKET] = 0
        precedence[self.RIGHT_BRACKET] = 0

        stack = list()
        output = list()

        for token in infix_token:
            if token == self.LEFT_BRACKET:
                stack.append(token)
            elif token == self.RIGHT_BRACKET:
                op = stack.pop()
                while op != self.LEFT_BRACKET:
                    output.append(op)
                    op = stack.pop()
            elif token in precedence:
                if stack:
                    current_op = stack[-1]
                    while stack and precedence[current_op] > precedence[token]:
                        output.append(stack.pop())
                        if stack:
                            current_op = stack[-1]
                stack.append(token)
            else:
                output.append(token.lower())

        while stack:
            output.append(stack.pop())

        return output

    def _fix_query(self, infix_query):
        """
        normalizing query in to tokens
        :param infix_query:
        :return:
        """
        infix_query = infix_query.replace('(', '( ')
        infix_query = infix_query.replace(')', ' )')
        infix_token = infix_query.split(' ')
        return infix_token

    @staticmethod
    def get_doc_idx(token, inverted_index):
        if inverted_index.get(token) is not None:
            return inverted_index.get(token)[1]
        else:
            return []

    @staticmethod
    def not_operator(list1, inverted_index):
        referenced_list = list()
        for _, value in inverted_index.items():
            referenced_list.extend(value[1])
        referenced_list = set(referenced_list)
        result = not_operator(list1, referenced_list)
        return result

    def process_query(self, query, inverted_index):
        tokens = self._fix_query(infix_query=query)

        stack = list()
        postfix_queue = deque(self._postfix(tokens))
        print(postfix_queue)
        while postfix_queue:
            token = postfix_queue.popleft()
            if token != self.AND_TOKEN and token != self.OR_TOKEN and token != self.NOT_TOKEN:
                stack.append(Search.get_doc_idx(token=token, inverted_index=inverted_index))
                print(stack)
            elif token == self.AND_TOKEN:
                list_1 = stack.pop()
                list_2 = stack.pop()
                result = intersect(list_1, list_2)
                stack.append(result)
            elif token == self.OR_TOKEN:
                list_1 = stack.pop()
                list_2 = stack.pop()
                result = union(list_1, list_2)
                stack.append(result)
            else:
                list_1 = stack.pop()
                stack.append(Search.not_operator(list_1, inverted_index=inverted_index))
        print(stack)
        stack_result = [ls for ls in stack if len(ls)>0]
        print(stack_result)
        if len(stack_result) > 1:
            print("Not valid query")
        return stack_result.pop()


