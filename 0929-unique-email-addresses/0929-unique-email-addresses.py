class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        distinct_emails = []
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if local.find('+') != -1:
                plus_index = local.find('+')
                local = local[:plus_index]
            simplified_email = local + '@' + domain
            if simplified_email not in distinct_emails:
                distinct_emails.append(simplified_email)
        return len(distinct_emails)