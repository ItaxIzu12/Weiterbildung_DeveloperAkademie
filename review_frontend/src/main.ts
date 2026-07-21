import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { ReviewComponent } from './app/review/review.component';

bootstrapApplication(ReviewComponent, appConfig)
  .catch((err) => console.error(err));
