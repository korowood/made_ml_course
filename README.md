# made_ml_course

## hw2
The task is to predict the genre of the film by a provided dialogue. We have 20 genres in total. Each film can have several genres (Multilabel classification).
The competition is assessed using the Mean F1-Score. For local validation, you can use the sklearn.metrics.f1_score (true, preds, average = 'samples') function

The evaluation metric for this competition is Mean F1-Score. The F1 score, commonly used in information retrieval, measures accuracy using the statistics 
precision p and recall r. Precision is the ratio of true positives (tp) to all predicted positives (tp + fp). Recall is the ratio of true positives to all 
actual positives (tp + fn).

The F1 metric weights recall and precision equally, and a good retrieval algorithm will maximize both precision and recall simultaneously. 
Thus, moderately good performance on both will be favored over extremely good performance on one and poor performance on the other.

**Результат**: топ 61

## hw3

В соревновании требуется спрогнозировать цены на недвижимость (аренда квартир) на сервисе airbnb в Лондоне.

Для построения модели доступны следующие данные:

 - Review - резюме отзывов для объявлений об аренде
 - Calendar - подробные календарные данные для объявлений об аренде
 - Train/Test - описание объявления об аренде.
 
 В этом соревновании используется метрика MAPE
 
 **Результат**: топ 2
 
 ## hw4
 
 ссылка на демо - https://github.com/korowood/demo_NBA_salaries
