# Print coefficients
coefficients = id.DataFrame({'Feature': features, 'Coefficient': model.coef_})
coefficients = coefficients.append({'Feature': 'Intercept', 'Coefficient': model.intercept_}, ignore_index=True)
print(coefficients)

# Find feature with the largest magnitude coefficient
most_important_feature = coefficients.loc[coefficients['Coefficient'].abs().idxmax()]
print("Most important feature:", most_important_feature['Feature'])
