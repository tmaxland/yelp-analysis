import yelp_analysis_tools as yat 

dataset_business = "datasets/head_yads_business.json"
dataset_user = "datasets/head_yads_user.json"
dataset_review = "datasets/head_yads_review.json"

# reviews, businesses, users = yat.importJSON(dataset) 
businesses  = yat.importBusinessesJSON(dataset_business)
users       = yat.importUsersJSON(dataset_user)
reviews     = yat.importReviewsJSON(dataset_review)


prolificUsers = [u['user_id'] for u in users if u['review_count'] > 0] 
# print len(prolificUsers)
prolificUsersReviewDates = [r['date'] for r in reviews if r['user_id'] in prolificUsers]

# print prolificUsersReviewDates
prolificUsersReviewDays = yat.convertDatesToDays(prolificUsersReviewDates) 
# print prolificUsersReviewDays
prolificDays = yat.get_counts(prolificUsersReviewDays) 
print prolificDays
yat.buildBarDayPlot(prolificDays, title="Days Prolific Users Reviewed Businesses")
