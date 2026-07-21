import { Component, signal } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ReviewService } from '../service/reviewService';

@Component({
  selector: 'reviewComponent',
  imports: [ReactiveFormsModule],
  templateUrl: './review.component.html',
  styleUrl: './review.component.scss'
})
export class ReviewComponent {
  review: FormGroup
  fb: FormBuilder = new FormBuilder;
  status = signal('');

  constructor(private readonly reviewService: ReviewService) {
    this.review = this.fb.group({
        firstName: ['', Validators.required],
        lastName: ['', Validators.required],
        message: ['', Validators.required]
    })
  }

  onSubmit() {
    console.log(this.review.value)
    this.reviewService.sendReview(this.review.value).subscribe({
      next: () => {
        this.status.set('Bewertung gesendet!');
        this.review.reset();
      },
      error: () => {
        this.status.set('Fehler beim Senden.');
      }
    });
  }
}
