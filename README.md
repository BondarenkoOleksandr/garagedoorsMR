# Garage Doors Multiregional
Backend for Garage Doors Multiregional

# API Links

## Articles
Get all articles - api/articles/

Get single article by id - api/articles/<int:id>/

Get single article by slug api/articles/<slug:your_slug>/

### Rating
Set single article rating - api/set_rating/<int:article_id>/

### Comments
Get all article comments - api/get_comments/<int:article_id>/

## Cities
Get all cities - api/cities/

Get single city - api/cities/<int:id>/

## States

Get all states - api/states/

Get single state - api/states/<int:id>/

## Employees
Get all employees - api/employees/

Get single employee - api/employees/id/

Create review - api/employee/create_review/
                
    api/employee/create_review/?name=Test&text=Test&rating=5&employee=32

    args - name, text, rating(Int), employee(Int)

