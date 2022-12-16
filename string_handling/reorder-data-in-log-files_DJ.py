class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = list(), list()
        numeric = list(map(str, range(10)))

        for log in logs:
            if any([True for _ in list(log.split()[1]) if _ in numeric]):
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        sort_letters = [pair[1] for pair in sorted([(" ".join(log.split()[1:]), log) for log in letter_logs])]

        return sort_letters + digit_logs