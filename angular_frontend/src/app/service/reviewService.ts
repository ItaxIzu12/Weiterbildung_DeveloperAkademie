import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Review {
  firstName: string;
  lastName: string;
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class ReviewService {
  private readonly apiUrl = 'http://localhost:8000/chat/';

  constructor(private readonly httpClient: HttpClient) {}

  sendReview(review: Review): Observable<Review> {
    return this.httpClient.post<Review>(this.apiUrl, review);
  }

  getReviews(): Observable<Review[]> {
    return this.httpClient.get<Review[]>(this.apiUrl);
  }
}
