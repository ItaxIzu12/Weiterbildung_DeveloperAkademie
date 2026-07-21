import { Component, OnInit, signal } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ReviewService, Review } from '../service/reviewService';

@Component({
  selector: 'reviewComponent',
  imports: [ReactiveFormsModule],
  templateUrl: './review.component.html',
  styleUrl: './review.component.scss'
})
export class ReviewComponent implements OnInit {
  review: FormGroup
  fb: FormBuilder = new FormBuilder;
  status = signal('');
  reviews = signal<Review[]>([]);

  constructor(private readonly reviewService: ReviewService) {
    this.review = this.fb.group({
        firstName: ['', Validators.required],
        lastName: ['', Validators.required],
        message: ['', Validators.required]
    })
  }

  ngOnInit() {
    this.loadReviews();
  }

  loadReviews() {
    this.reviewService.getReviews().subscribe({
      next: (reviews) => {
        this.reviews.set(reviews);
      },
      error: () => {
        this.status.set('Bewertungen konnten nicht geladen werden.');
      }
    });
  }

  onSubmit() {
    if (this.review.invalid) {
      this.review.markAllAsTouched();
      this.status.set('Bitte alle Felder ausfüllen.');
      return;
    }

    this.reviewService.sendReview(this.review.value).subscribe({
      next: () => {
        this.status.set('Bewertung gesendet!');
        this.review.reset();
        this.loadReviews();
      },
      error: () => {
        this.status.set('Fehler beim Senden.');
      }
    });
  }
}
