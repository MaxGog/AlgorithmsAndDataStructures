using System.Text;

using ListBooks.Models;

namespace ListBooks.Data;

public class BookData
{
    private const string BOOK_SEPARATOR = "---";
    private readonly List<CardModel> Books = new();
    public List<CardModel> GetBooks() => Books;

    public async Task AddContentAsync()
    {
        try
        {
            using var stream = await FileSystem.OpenAppPackageFileAsync("Books.txt");
            using StreamReader reader = new(stream, Encoding.UTF8);
            int idCounter = 1;
            string line = await reader.ReadLineAsync();

            do {
                if (!string.IsNullOrWhiteSpace(line))
                {
                    if (line.Trim() == BOOK_SEPARATOR)
                    {
                        var bookData = await ReadBookData(reader);
                        if (!string.IsNullOrWhiteSpace(bookData.NameBook))
                        {
                            Books.Add(new CardModel
                            {
                                Id = idCounter++,
                                NameBook = bookData.NameBook.Trim(),
                                Author = bookData.Author.Trim(),
                                PublicationDate = DateTime.Parse(bookData.PublicationDate.Trim()),
                                PublicationPlace = bookData.PublicationPlace.Trim(),
                                Description = bookData.Description.Trim()
                            });
                        }
                    }
                }
            } while ((line = await reader.ReadLineAsync()) != null);
        }
        catch (Exception ex)
        {
            await Application.Current.MainPage.DisplayAlert("Ошибка!", $"Ошибка при чтении файла: {ex.Message}", "OK");
        }
    }

    private async Task<(string NameBook, string Author, string PublicationDate, string PublicationPlace, string Description)> ReadBookData(StreamReader reader)
    {
        try
        {
            string nameBook = await reader.ReadLineAsync() ?? "";
            string author = await reader.ReadLineAsync() ?? "";
            string publicationDate = await reader.ReadLineAsync() ?? "";
            string publicationPlace = await reader.ReadLineAsync() ?? "";
            StringBuilder description = new();
            string line;
            while ((line = await reader.ReadLineAsync()) != null)
            {
                if (line.Trim() == BOOK_SEPARATOR)
                {
                    break;
                }
                description.AppendLine(line);
            }

            return (
                NameBook: nameBook,
                Author: author,
                PublicationDate: publicationDate,
                PublicationPlace: publicationPlace,
                Description: description.ToString().Trim()
            );
        }
        catch (Exception ex)
        {
            await Application.Current.MainPage.DisplayAlert("Ошибка!", $"Ошибка при чтении данных книги: {ex.Message}", "OK");
            return (
                NameBook: string.Empty,
                Author: string.Empty,
                PublicationDate: string.Empty,
                PublicationPlace: string.Empty,
                Description: string.Empty
            );
        }
    }
}