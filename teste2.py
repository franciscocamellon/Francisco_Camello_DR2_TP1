# rule = {"Atributo com domínio incorreto": {"hid_trecho_drenagem_l": {"allRules": ["regime in (999)"]}}}
rule = {"Atributo com domínio incorreto": {"hid_trecho_drenagem_l": {"allRules": ("regime in (999)")}}}

def validateRuleFormat(rule):
    """
    This function evaluates the rule format from both rules input
    and inform to user if it's ok or not.
    """
    if isinstance(rule, dict):
        for description in rule.values():
            if isinstance(description, dict):
                for layer in description.values():
                    if isinstance(layer, dict):
                        for rules in layer.values():
                            if isinstance(rules, list):
                                print('Regra segue o formato padrão!')
                            else:
                                print('Regra não segue o formato padrão!')
                    else:
                        print('Regra não segue o formato padrão!')
            else:
                print('Regra não segue o formato padrão!')
    else:
        print('Regra não segue o formato padrão!')


validateRuleFormat(rule)