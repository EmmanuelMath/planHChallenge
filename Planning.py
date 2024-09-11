from data_planning import universal_category_list, \
other_categories, YES, NO, location_of_item

class Planning:
    def __init__(self, category, height=None, itemPosition=None):
        self.category = category
        self.height = height
        self.itemPosition = itemPosition

    def check_permission(self):
        validating_string = self.category.upper().strip()
        if not validating_string in universal_category_list:
            raise Exception(f"Site {validating_string} Not In This Category")
        if validating_string in universal_category_list:
            return f"Permission Required For Site Category: {validating_string}"
        else:
            return f"Permission Might Not Be Required For Site {validating_string}"

    def check_sepcific_permission(self):
        validating_string = self.category.upper().strip()

        if not validating_string in other_categories:
            raise Exception(f"Site {validating_string} Not In This Category")
        if validating_string in other_categories:
            if self.itemPosition and self.height > 1:
                return f"Permission Required For Site Category: {validating_string}"
            elif self.height > 2:
                return f"Permission Required For Site Category: {validating_string}"
            else:
                return f"Permission Might not be required For Site Category: {validating_string}"

