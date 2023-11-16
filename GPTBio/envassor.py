import json

class Envassor:
    """
    Envassor是在LLM中与lexobe交流的实体，代表了环境评估者的角色。Envassor的主要职责是给出特定的题目，并根据lexobe的回答来评估其表现。
    """
    def __init__(self, questions_file):
        """
        初始化Envassor类，从JSON文件中读取问题。

        参数:
            questions_file (str): 包含问题的JSON文件的路径。
        """
        with open(questions_file, 'r') as file:
            self.questions = json.load(file)
        self.current_question_index = 0

    def talk_with(self, lexobe):
        """
        与lexobe交流，提出问题并评估回答。

        参数:
            lexobe (Lexobe): 要交流的lexobe。
        """
        while True:
            question = self.ask_question()
            if question is None:
                break
            answer = lexobe.answer_question(question)
            evaluation = self.evaluate_answer(question, answer)
            lexobe.receive_evaluation(evaluation)
                                      
    def ask_question(self):
        """
        提出下一个问题。当所有问题都已经提出时，返回一个通知信息。

        返回:
            dict: 下一个问题的JSON结构，或者通知信息，表明没有更多的问题。
        """
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        else:
            return None

    def evaluate_answer(self, answer):
        """
        评估给定的回答。具体的评估逻辑可以根据实际需求添加。

        参数:
            answer (str): 要评估的回答文本。

        返回:
            str: 代表评估结果的文本或分数。具体形式可以根据需要自定义。
        """
        # 你可以在此处添加具体的评估逻辑，比如与标准答案的比较等
        evaluation = "Assessment for the answer"  # 这里可以是具体的评价或分数
        return evaluation
