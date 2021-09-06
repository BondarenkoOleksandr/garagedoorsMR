# Garage Doors Multiregional
Backend for Garage Doors Multiregional

# API Links

## Articles
Get all articles - api/articles/

Get single article by id - api/articles/<int:id>/?rating=<int:rating>

Get single article by slug - api/articles/<slug:your_slug>/

Get articles by tags - api/articles/by_tags/?tags=wolf,cat,dog

### Rating
Set single article rating - api/set_rating/<int:article_id>/

### Comments
Get all article comments - api/get_comments/<int:article_id>/

### Tags

Get all tags - api/tags/

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

# Services

Get all services - api/services/

Get all services categories - api/services/categories/

Get all services in category by slug - api/services/category/<slug:slug>/

Get single service by slug - api/services/<slug:slug>/
   
# Reviews

Get all reviews - api/reviews/

Get single review - api/reviews/<int:id>/

# Registration/Login

486436967116-tiadudc1f9rmoj9c94rgp86q5ppks5pb.apps.googleusercontent.com - clientId
